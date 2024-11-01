# Import the boto3 module
import boto3
# Open Management console
aws_management_console = boto3.session.Session(profile_name="default")
# open ec2 console
ec2_console = aws_management_console.client('ec2')
# create the ec2 instance
create_instance = ec2_console.run_instances(
    ImageId='ami-###################',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
)

# To stop Ec2 Instance:
stop_ec2_instance = ec2_console.stop_instance(
    InstanceIds=['ami-##############']
)