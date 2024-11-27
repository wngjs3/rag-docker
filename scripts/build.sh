#!/bin/bash

ENV=$1
if [ -z "$ENV" ]; then
    ENV="dev"
fi

echo "Building for $ENV environment..."
docker-compose -f docker-compose.$ENV.yml build 