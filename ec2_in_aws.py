# Import the boto3 module
import boto3
# Open Management console
aws_management_console = boto3.session.Session(profile_name="default")
# open ec2 console
ec2_console = aws_management_console.client(service_name='ec2')
# To list instances
list_instances = ec2_console.describe_instances()
print(list_instances)
