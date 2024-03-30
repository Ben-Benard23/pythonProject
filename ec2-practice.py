import boto3

client = boto3.client('ec2', region_name="ca-central-1")

response = client.run_instances(
    ImageId='ami-0156b61643fdfee5c',
    MaxCount=1,
    MinCount=1,
    InstanceType="t2.micro",
    TagSpecifications=[
              {
                'ResourceType': 'instance',
                'Tags' : [
                     {
                      'Key': 'Name',
                      'Value': 'Bot-instance'
                    },
                ]
             },
    ],
)
print(response)