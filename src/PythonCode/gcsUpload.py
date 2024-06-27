from gcloud import storage

storage_client = storage.client()

bucket = storage_client.get_bucket('bkt_data_source_mt_devops') # This bucket is created via Terraform.
blob = bucket.blob('test/newTest.txt')
blob.upload_from_filename('./data/text.txt')