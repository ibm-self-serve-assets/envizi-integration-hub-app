#!/usr/bin/env bash

podman run -d -p 3001:3001 --name my-e-int-hub3 \
    --env LOGLEVEL=DEBUG \
    --env DATA_FOLDER="/app/data" \
    --env DATA_STORE_FOLDER="/app/data" \
    --env OUTPUT_FOLDER="/app/output" \
    -v "/root/int-hub/envizi-config.json:/app/envizi-config.json" \
    gandigit/e-int-hub3-linux:latest

echo "build completed ...."