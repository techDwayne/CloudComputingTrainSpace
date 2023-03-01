import boto3
#create an  IAM client
iam = boto3.client('iam')

#Create a user
response = iam.create_user(UserName='testuser')

print(response)
