#!/usr/bin/env bash

echo "run Started ...."

DOCKER_IMAGE=gandigit/e-int-hub3-ui-linux

cd ../web

podman run -d -p 3000:3000 --name my-e-int-hub3-ui --env NEXT_PUBLIC_API_URL="http://localhost:3001"  $DOCKER_IMAGE:latest

echo "run completed ...."