import os
from botocore.exceptions import BotoCoreError, ClientError
from utils.init_client import init_client

def upload_file(bucket_name, file_name):
    s3_client = init_client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket_name, os.path.basename(file_name))
        print(f"File {file_name} uploaded to {bucket_name}.")
    except (BotoCoreError, ClientError) as error:
        print(f"An error occurred while uploading file to bucket: {error}")