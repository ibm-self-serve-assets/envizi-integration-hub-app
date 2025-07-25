#!/usr/bin/env bash

echo "docker run Started ...."

# podman run -d -p 3001:3001 --name my-e-int3-hub \
#     --env LOGLEVEL=DEBUG \
#     -v "/Users/gandhi/GandhiMain/700-Apps/envizi-integration-hub/app/envizi-config.json:/app/envizi-config.json" \
#     gandigit/e-int-hub-1-mac:latest


podman run -d -p 3001:3001 --name my-e-int-hub3 \
    --env LOGLEVEL=DEBUG \
    --env DATA_FOLDER="/app/data" \
    --env DATA_STORE_FOLDER="/app/data" \
    --env OUTPUT_FOLDER="/app/output" \
    -v "/Users/gandhi/GandhiMain/700-Apps/envizi-integration-hub-app/api/config/envizi-config.json:/app/envizi-config.json" \
    gandigit/e-int-hub3-mac:latest


echo "run completed ...."