import logging 
from os import environ
from waitress import serve

from student_enrollment import (
    celery,
    create_app
)
# from student_enrollment.controllers import monitoring
# from student_enrollment.models import logs
# 

# logs.setup_logging('info')


if __name__ == '__main__':
    port = environ.get('COMPONENT_PORT', 8081)
    app = create_app()
    # monitor = monitoring.TasksMonitoring(app)
    # monitor.start()
    try:
        serve(app, host='0.0.0.0', port=port)
    except (KeyboardInterrupt, SystemExit):
        logging.getLogger().warning("The application is stopping!")
        # monitor.stop()
        raise
