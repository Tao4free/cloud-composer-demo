#!/usr/bin/env bash

if [[ $# -eq 0 ]] ; then
    echo 'Need parameters: GCS bucket name, composer environment name。'
    exit 0
fi

bucket_name="$1"
composer_env_name="$2"
gsutil mb gs://$bucket_name
gcloud composer environments update $composer_env_name \
    --update-pypi-packages-from-file requirements.txt
    --location asia-northeast1 \
    --update-env-variables=UPLOAD_GCS_BUCKET_NAME=$bucket_name || true

gcloud composer environments storage dags import \
  --environment $composer_env_name \
  --location asia-northeast1 \
  --source create_upload_gcs.py
