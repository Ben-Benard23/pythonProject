# import boto3
# #step1
# import boto3
#
# #step 2 is get client
# client = boto3.client('ec2')

#choose method "run_instance"
#copy what is required in the request syntax, then the response syntax

import boto3
client = boto3.client('ec2', region_name="ca-central-1")

response = client.run_instances(

    ImageId='ami-0b47e94e754413bcb',
    InstanceType='t2.micro',
    KeyName='my-centralcanada-key',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-0a7a4a1bc2fe38588',
    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'testcreatedbypython',
                },
            ],
        },
    ],
)
print(response)