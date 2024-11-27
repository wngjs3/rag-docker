#!/bin/bash

ENV=$1
if [ -z "$ENV" ]; then
    ENV="dev"
fi

echo "Accessing shell in api container..."
docker-compose -f docker-compose.$ENV.yml exec api /bin/bash 