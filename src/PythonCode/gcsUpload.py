# from gcloud import storage
from google.cloud import storage

# Initialize a client
# storage_client = storage.client()
storage_client = storage.Client()

# List all buckets
buckets = storage_client.list_buckets()
for bucket in buckets:
    print(bucket.name)

# Upload a file to a bucket
bucket = storage_client.get_bucket('bkt_data_source_mt_devops') # This bucket is created via Terraform.
blob = bucket.blob('test/newTest.txt')
blob.upload_from_filename('./data/text.txt')