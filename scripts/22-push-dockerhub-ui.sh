#!/usr/bin/env bash

echo "push Started ...."

DOCKER_IMAGE=gandigit/e-int-hub3-ui

cd ../api

### Linux
podman push $DOCKER_IMAGE-linux:latest

# ### Mac
# podman push $DOCKER_IMAGE-mac:latest

echo "push completed ...."