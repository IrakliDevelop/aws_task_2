# AWS CLI Script

This script provides a command line interface for managing AWS services. The script supports the following operations:

- Upload a file to a specified S3 bucket.
- Create a private subnet within a specified VPC.
- Authorize SSH access from the machine running the script to an EC2 instance specified by security group ID.

## Prerequisites

- Python 3.7 or higher.
- Poetry for managing dependencies.
- An AWS account with appropriate permissions for the operations you want to perform.
- AWS credentials configured on your machine, either by defining environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION`, or by using the [AWS CLI configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/IrakliDevelop/aws_task_2.git
cd aws_task_2
```

2. Install dependencies:

```bash
poetry install
```

## Usage

All commands should be preceded by `poetry run python main.py`.

1. Upload a file to a bucket:

```bash
poetry run python main.py bucket <bucket_name> -upload_file <file_name>
```

2. Create a private subnet in a VPC:

```bash
poetry run python main.py vpc <VpcId> -create_private_subnet <cidr_block>
```

3. Add SSH access for current machine to a specified security group:

```bash
poetry run python main.py ec2 -security_group_id <sg_id> -ssh_my_ip
```

For help with the command-line options, you can use the `-h` or `--help` options with the script or any of its commands.

