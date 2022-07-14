import json

import boto3
import pprint as pp

s3_client = boto3.client('s3')

s3_resource = boto3.resource('s3')

bucket_list = s3_client.list_buckets()

# get all buckets
# pp.pprint(bucket_list)

# for bucket in bucket_list['Buckets']:
#     print(bucket['Name'])


# # look inside one bucket
bucket_name  = 'data-eng-resources'
bucket_contents = s3_client.list_objects(Bucket=bucket_name, Prefix='python')
pp.pprint(bucket_contents)

for object in bucket_contents['Contents']:
    print(object['Key'])

# s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/chatbot-intent.json')
#
# strBody = s3_object['Body']
#
# pp.pprint(json.load(strBody))
