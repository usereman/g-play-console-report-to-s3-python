from io import StringIO # python3; python2: BytesIO
import boto3
import os
from google.cloud import storage
import pandas as pd
import io

# Path to private_key.json which is in project root directory
jsonfile = os.path.join(
    os.path.dirname(__file__), 'private_key.json')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= jsonfile

# Enter your bucket name below
bucket_name = 'pubsite_prod_rev_####################'
# Enter your file path below (the one you want to fetch)
source_blob_name = 'stats/installs/installs_com.kn.your.game.name_202110_country.csv'

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)
data = blob.download_as_string()
df = pd.read_csv(io.BytesIO(data),encoding='utf-16')

#print(df)  # Uncomment this line if you want to print result


# The code below gets csv data from dataframe (df) and uploads it to your s3 bucket

# Enter your s3 bucket name below
bucket = 'S3BucketName' # already created on S3
csv_buffer = StringIO()
df.to_csv(csv_buffer)

# ( I have created separate IAM user for this purpose and you can follow more secure way to do this. )
# Enter your IAM user access key ID and secret access key below.

s3_resource = boto3.resource('s3', aws_access_key_id='##########',aws_secret_access_key = '#################')
s3_resource.Object(bucket, 'file_name.csv').put(Body=csv_buffer.getvalue())
