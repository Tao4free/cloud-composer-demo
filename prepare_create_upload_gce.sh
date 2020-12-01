#!/usr/bin/env bash

if [[ $# -eq 0 ]] ; then
    echo 'Please enter one parameter for GCS bucket name。'
    exit 0
fi

bucket_name="$1"
gsutil mb gs://$bucket_name
gcloud composer environments update wills-composer-demo \
    --update-env-variables=[UPLOAD_GCS_BUCKET_NAME=$bucket_name]
