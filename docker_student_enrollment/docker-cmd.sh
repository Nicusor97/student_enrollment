ME=`basename "StudentEnrollment: docker-cmd.sh"`

if [ -z "$DOCKER_EXEC_COMMAND" ]; then
    echo "$ME: \$DOCKER_EXEC_COMMAND is set to the empty string"
else
    echo "$ME: \$DOCKER_EXEC_COMMAND has the value: $DOCKER_EXEC_COMMAND"
fi

if [ -z "$DOCKER_EXEC_FILE" ]; then
    echo "$ME: \$DOCKER_EXEC_FILE is set to the empty string"
else
    echo "$ME: \$DOCKER_EXEC_FILE has the value: $DOCKER_EXEC_FILE"
fi

if [ -z "$DOCKER_EXEC_ARGS" ]; then
    echo "$ME: \$DOCKER_EXEC_ARGS is set to the empty string (most likely ok!)"
else
    echo "$ME: \$DOCKER_EXEC_ARGS has the value: $DOCKER_EXEC_ARGS"
fi

echo "$ME: Starting Component with command exec $DOCKER_EXEC_COMMAND $DOCKER_EXEC_FILE $DOCKER_EXEC_ARGS"
exec $DOCKER_EXEC_COMMAND $DOCKER_EXEC_FILE $DOCKER_EXEC_ARGS
