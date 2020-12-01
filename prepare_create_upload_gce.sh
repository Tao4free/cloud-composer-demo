#!/usr/bin/env bash

if [[ $# -eq 0 ]] ; then
    echo 'Please enter one parameter for GCS bucket name。'
    exit 0
fi

bucket_name="$1"
composer_env_name="$2"
gsutil mb gs://$bucket_name
gcloud composer environments update $composer_env_name \
    --update-env-variables=[UPLOAD_GCS_BUCKET_NAME=$bucket_name]
