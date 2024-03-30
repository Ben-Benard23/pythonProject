
#step1
import boto3
client = boto3.client('ec2', region_name="us-east-2")

#choose method launch instance
response = client.run_instances(
    ImageId='ami-019f9b3318b7155c5',
    MaxCount=1,
    MinCount=1,
    InstanceType="t2.micro",
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            "Tags" : [
                {
                    'Key': 'Name',
                    'Value': 'EC2-Python'
                },
            ]
        },
    ],
)
print(response)