import boto3

aws_management_console = boto3.session.Session(profile_name="default")
iam_console_resource = aws_management_console.resource('iam')
iam_console_client = aws_management_console.client('iam')

# IAM Users list using resource object:
for each_user in iam_console_resource.users.all():
    print(each_user.name)

# IAM  Users list using client object:
for each in iam_console_client.list_users()['Users']:
    print(each['UserName'])

"""
    The session is the AWS management console. It saves configurations and allows us create services, clients and resources.
    Resources and Clients enables you to create a particular AWS Service. 
    You can also specifywhich region where you want the service to be created
    To get the resource objects: 
    aws_management_console = boto3.session.Session(profile_name="default")
    dir(aws_management_console)
    print(aws_management_console.get_available_resources())
    All Operations on the AWS management console can be done using the CLIENT whereas, Resources does not guaratee that. It is not supported for all the services.
    """