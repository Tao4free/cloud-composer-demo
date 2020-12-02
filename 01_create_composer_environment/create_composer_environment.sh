#!/usr/bin/env bash
source ../config.sh

gcloud composer environments create ${COMPOSER_ENV_NAME} \
    --location ${LOCATION} \
    --zone ${ZONE} \
    --python-version 3
