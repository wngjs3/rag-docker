#!/bin/bash

ENV=$1
if [ -z "$ENV" ]; then
    ENV="dev"
fi

echo "Stopping services for $ENV environment..."
docker-compose -f docker-compose.$ENV.yml down 