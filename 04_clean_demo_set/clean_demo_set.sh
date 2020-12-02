#!/usr/bin/env bash
source ../config.sh

composer_gcs_entry=`gcloud composer environments describe ${COMPOSER_ENV_NAME} --location ${LOCATION} | grep dagGcsPrefix`
composer_gcs_path=${webserver_res##*' '}

gcloud composer environments delete ${COMPOSER_ENV_NAME}

gcloud functions delete gcs-dag-trigger-function

gsutil rm -r gs://${composer_gcs_path}
gsutil rm -r gs://${UPLOAD_GCS_BUCKET_NAME}
