#!/usr/bin/env bash

echo "build Started ...."

DOCKER_IMAGE=gandigit/e-int-hub3-ui

cd ../web

### Linux
# podman build --no-cache --platform linux/amd64 -f Dockerfile -t $DOCKER_IMAGE-linux:latest .
# podman push $DOCKER_IMAGE-linux:latest

# ### Mac
podman build --no-cache --platform linux/arm64 -f Dockerfile -t$DOCKER_IMAGE-mac:latest .
# podman push $DOCKER_IMAGE-mac:latest

echo "build completed ...."


