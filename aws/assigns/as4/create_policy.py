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
        print('Something went wrong init iam client.')
    return None


def create_new_policy(policy_name, policy_filename):
    client = iam_init_client()
    if client:
        try:
            file = open(policy_filename, 'r')
            policy_json = json.load(file)
            jsonp = json.JSONEncoder().encode(policy_json)
            response = client.create_policy(PolicyName=policy_name, PolicyDocument=jsonp)
            print(response)
        except FileNotFoundError:
            print('No credentials file found.')
        except:
            print('Something went wrong creating new policy.')        

create_new_policy('test-policy-as4-python', 'policy.json')