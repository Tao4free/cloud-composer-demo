#!/usr/bin/env bash
source ../config.sh

gcloud composer environments storage dags import \
  --environment ${COMPOSER_ENV_NAME} \
  --location ${LOCATION} \
  --source create_upload_gcs_failed_handling.py




