from botocore.exceptions import BotoCoreError, ClientError
from utils.init_client import init_client

def create_private_subnet(vpc_id, cidr_block):
    ec2_client = init_client('ec2')
    try:
        response = ec2_client.create_subnet(VpcId=vpc_id, CidrBlock=cidr_block, MapPublicIpOnLaunch=False)
        print(f"Created private subnet {response['Subnet']['SubnetId']} in VPC {vpc_id} with CIDR block {cidr_block}.")
    except (BotoCoreError, ClientError) as error:
        print(f"An error occurred while creating private subnet: {error}")
