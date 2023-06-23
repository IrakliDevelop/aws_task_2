import argparse
from aws_cli.bucket_operations import upload_file
from aws_cli.vpc_operations import create_private_subnet
from aws_cli.ec2_operations import ssh_my_ip

def main():
    parser = argparse.ArgumentParser(description='AWS CLI')
    subparsers = parser.add_subparsers()

    # bucket subcommand
    bucket_parser = subparsers.add_parser('bucket', help='Bucket operations')
    bucket_parser.add_argument('bucket_name', help='Name of the bucket')
    bucket_parser.add_argument('-upload_file', required=True, help='File to upload')
    bucket_parser.set_defaults(func=upload_file)

    # vpc subcommand
    vpc_parser = subparsers.add_parser('vpc', help='VPC operations')
    vpc_parser.add_argument('VpcId', help='VPC Id')
    vpc_parser.add_argument('-create_private_subnet', required=True, help='CIDR block for the new subnet')
    vpc_parser.set_defaults(func=create_private_subnet)

    # ec2 subcommand
    ec2_parser = subparsers.add_parser('ec2', help='EC2 operations')
    ec2_parser.add_argument('-security_group_id', required=True, help='Security Group Id')
    ec2_parser.add_argument('-ssh_my_ip', action='store_true', help='Add SSH access for current IP to the security group')
    ec2_parser.set_defaults(func=ssh_my_ip)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')