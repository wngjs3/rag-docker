#!/bin/bash

ENV=$1
if [ -z "$ENV" ]; then
    ENV="dev"
fi

echo "Starting services for $ENV environment..."
docker-compose -f docker-compose.$ENV.yml up -d 