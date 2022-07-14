import pandas
import boto3


s3_client = boto3.client('s3')

# s3_resource = boto3.resource('s3')

# bucket_list = s3_client.list_buckets()
bucket_name = 'data-eng-resources'


def get_average(all_the_data):
    return all_the_data.groupby('Species')[
        ['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']].mean().reset_index()


def get_data_source():
    return s3_client.list_objects(Bucket=bucket_name, Prefix='python/fish')


data_merged = []


def go_through_bucket(bucket_content):
    for content in bucket_content['Contents']:
        data = content['Key']
        data_object = s3_client.get_object(Bucket=bucket_name, Key=data)
        data_content = pandas.read_csv(data_object['Body'])
        data_merged.append(data_content)
    return pandas.concat(data_merged)


def get_data():
    bucket_contents = get_data_source()

    return go_through_bucket(bucket_contents)


all_data = get_data()

averages = get_average(all_data)

print(averages)
#
# averages.to_csv('average.csv')
#
# s3_client = boto3.client('s3')
#
# s3_client.upload_file(
#     Filename="average.csv",
#     Bucket=bucket_name,
#     Key="Data30/MoShah/average.csv"
# )


