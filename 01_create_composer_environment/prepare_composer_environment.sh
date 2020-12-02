#!/usr/bin/env bash
source ../config.sh

gcloud composer environments create ${COMPOSER_ENV_NAME} \
    --location ${LOCATION} \
    --zone ${ZONE} \
    --env-variables=UPLOAD_GCS_BUCKET_NAME=${UPLOAD_GCS_BUCKET_NAME} \
    --python-version 3
