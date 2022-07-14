import json
import boto3
import pprint as pp

s3_client = boto3.client('s3')

s3_resource = boto3.resource('s3')

bucket_list = s3_client.list_buckets()

bucket_name  = 'data-eng-resources'

# dict_to_upload = {'name':'data','status':1}
#
# with open("data.json", 'w') as jsonFile:
#     json.dump(dict_to_upload, jsonFile)

s3_client.upload_file(
    Filename="data.json",
    Bucket=bucket_name,
    Key="Data30/Test/MoShah/data.json"
)
