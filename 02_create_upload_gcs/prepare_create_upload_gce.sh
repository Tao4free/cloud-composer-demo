#!/usr/bin/env bash
source ../config.sh

gsutil mb gs://${UPLOAD_GCS_BUCKET_NAME}

# gcloud composer environments update ${COMPOSER_ENV_NAME} \
    # --location ${LOCATION} \
    # --update-pypi-packages-from-file requirements.txt || true

gcloud composer environments update ${COMPOSER_ENV_NAME} \
    --location ${LOCATION} \
    --update-env-variables=UPLOAD_GCS_BUCKET_NAME=${UPLOAD_GCS_BUCKET_NAME} || true

gcloud composer environments storage dags import \
  --environment ${COMPOSER_ENV_NAME} \
  --location ${LOCATION} \
  --source pendulum

gcloud composer environments storage dags import \
  --environment ${COMPOSER_ENV_NAME} \
  --location ${LOCATION} \
  --source create_upload_gcs.py
