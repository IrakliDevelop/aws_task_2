import requests
from botocore.exceptions import BotoCoreError, ClientError
from utils.init_client import init_client

def ssh_my_ip(security_group_id):
    ec2_client = init_client('ec2')
    try:
        my_ip = requests.get('https://api.ipify.org').text
        response = ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': f"{my_ip}/32"}]
                }
            ]
        )
        print(f"Added SSH access for IP {my_ip} to security group {security_group_id}.")
    except (BotoCoreError, ClientError, requests.RequestException) as error:
        print(f"An error occurred while adding SSH access to security group: {error}")