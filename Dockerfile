FROM python:3.8.3-slim-buster

# Required Args
ARG VERSION

# MANDATORY - UBISERVICES.SHIPYARD PLATFORM SECTION - You should modify the values only!
#
ENV DOCKER_EXEC_COMMAND=python
ENV DOCKER_EXEC_FILE=run.py
# DOCKER_EXEC_ARGS="-a -b=allo -c"
ENV DOCKER_EXEC_ARGS=""

# Make sure image is up to date
RUN apt-get update && \
    apt-get install -y gcc make bash curl musl-dev libffi-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup script
WORKDIR /opt/us-app

# python specific
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY run.py ./
COPY apply_db_migrations.sh ./
# COPY migrations ./migrations
COPY student_enrollment ./student_enrollment

ENV PYTHONPATH /opt/us-app

#
# MANDATORY - UBISERVICES.SHIPYARD PLATFORM SECTION - DO NOT CHANGE OR REMOVE
#
# Copy platform files
COPY docker_student_enrollment ./
# Right permissions
RUN chmod a+x ./docker-cmd.sh ./apply_db_migrations.sh
# Clean the sh files (remove \r)
RUN for i in `find -type f -name "*.sh"`; do sed -i 's/\r//g' $i; echo "Removing Windows end of line for : $i"; done

# create logs files
RUN mkdir -p "student_enrollment/logs"

# Start
ENTRYPOINT ["./docker-cmd.sh"]
