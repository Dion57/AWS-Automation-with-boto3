import boto3

aws_management_console = boto3.session.Session(profile_name="default")
iam_console = aws_management_console.resource('iam')

for each_user in iam_console.users.all():
    print(each_user.name)


    #The session is the AWS management console. It saves configurations and allows us create services, clients and resources.
    #Resources and Clients enables you to create a particular AWS Service. 
    #You can also specifywhich region where you want the service to be created