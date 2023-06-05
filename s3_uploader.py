import os
from dotenv import load_dotenv
import boto3

load_dotenv()

def upload_file_to_s3(file_path, bucket_name, s3_key):
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to se://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading file: {str(e)}")

file_path = os.getenv("FILE_PATH")
bucket_name = os.getenv("BUCKET_NAME")
object_name = os.getenv("OBJECT_NAME")

upload_file_to_s3(file_path, bucket_name, object_name)


