# Create a Bucket to upload the file via Python Function

resource "google_storage_bucket" "bkt_data_source" {
  name = "bkt_data_source_mt_devops"
  location = "us-east1"
}