import logging
import os

from celery import Celery
from flask import Flask
from flask_caching import Cache
from flask_migrate import Migrate, upgrade
from flask_sqlalchemy import SQLAlchemy


LOGGER = logging.getLogger(__name__)

broker_addr = 'redis'

DB_USER = 'root'
DB_PASSWORD = 'root'
DB_ADDRESS = '127.0.0.1'
DB_PORT = 3306

MYSQL_ADDRESS = f'{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}:{DB_PORT}'


class AppConfig:
    CELERY_BROKER_URL = f'redis://{broker_addr}:6379'
    CELERY_RESULT_BACKEND = f'redis://{broker_addr}:6379'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TRACK_STARTED = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_ADDRESS}/studentsenrollment'


db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
celery = Celery(__name__, broker=AppConfig.CELERY_BROKER_URL)
celery.config_from_object(AppConfig)


def create_app(config_class=AppConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://' + broker_addr + "/1"})
    celery.conf.update(app.config)

    # for dev and prod, the migrations are applied before deployment, no need to run this code
    with app.app_context():
        migrations_dir = '/opt/us-app/migrations'

        if os.path.isdir(migrations_dir):
            # this removes current root logger handlers and adds a StreamHandler
            upgrade(directory=migrations_dir)

    from student_enrollment.views import student_enrollment

    app.register_blueprint(student_enrollment.app)
    return app
