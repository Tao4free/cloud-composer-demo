#!/usr/bin/env bash
source ../config.sh

composer_gcs_entry=`gcloud composer environments describe ${COMPOSER_ENV_NAME} --location ${LOCATION} | grep dagGcsPrefix`
composer_gcs_path=${composer_gcs_entry##*' '}
composer_gcs_path=${composer_gcs_path/\/dags//}

gcloud composer environments delete ${COMPOSER_ENV_NAME} --location ${LOCATION} --quiet

gcloud functions delete gcs-dag-trigger-function --quiet

gsutil rm -r  ${composer_gcs_path}
gsutil rm -r  gs://${UPLOAD_GCS_BUCKET_NAME}
