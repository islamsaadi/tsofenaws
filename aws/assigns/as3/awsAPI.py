import boto3
import json

def iam_init_client():
    try:
        file = open('secret_mykeys.json', 'r')
        mykeys = json.load(file)
        client = boto3.client('iam', aws_access_key_id=mykeys['aws_access_key_id'], 
                                        aws_secret_access_key=mykeys['aws_secert_access_key'],
                                        region_name=mykeys['region_name'])
        return client
    except FileNotFoundError:
        print('No credentials file found.')
    except:
        print('Something went wrong.')
    return None

def add_new_user(user_name):
    client = iam_init_client()
    if client:
        response = client.create_user(UserName = user_name)
        print(response)
    
def create_group_using_policy_path(group_name, policy_arn):
    client = iam_init_client()
    if client:
        response = client.create_group(GroupName=group_name)
        print(response)
        response = client.attach_group_policy(GroupName=group_name, PolicyArn=policy_arn)
        print(response)

def attach_user_to_group(user_name, group_name):
    client = iam_init_client()
    if client:
        response = client.add_user_to_group( GroupName=group_name,
                                            UserName=user_name)
        print(response)

user_name='newuser1'
group_name='NewDev1'
policy_path='arn:aws:iam::aws:policy/PowerUserAccess'

add_new_user(user_name)
create_group_using_policy_path(group_name, policy_path)
attach_user_to_group(user_name=user_name, group_name=group_name)

    