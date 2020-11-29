"""
Only used locally to generate migration files.
The migration file will be generated in "migrations/versions"

    Command: python manage.py db migrate --rev-id name_of_migration_file
"""
import getopt
import os
import sys

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


from student_enrollment import create_app, db, AppConfig


class LocalhostConfig(AppConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/studentsenrollment'


# Import all models so that alembic can see them
import student_enrollment.models.database

app = create_app(LocalhostConfig)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

MAX_MIGRATION_NAME_LENGTH = 32

if __name__ == '__main__':
    # the name of the migration file should not exceed 32 characters (the length of the `version_num` column
    # from `alembic_version` table), otherwise applying the migration will fail
    all_args = sys.argv[1:]
    if all_args[:2] == ['db', 'migrate']:
        opts, _ = getopt.getopt(sys.argv[3:], '', ['rev-id='])
        if opts and len(opts[0][1]) > MAX_MIGRATION_NAME_LENGTH:
            raise Exception(f'The name of the migration file cannot exceed {MAX_MIGRATION_NAME_LENGTH} characters.')

    manager.run()
