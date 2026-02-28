provider "aws" {
    region = "ap-south-1"
}


data "aws_iam_users" "users" {}

data "local_file" "foo"{
    filename = "${path.module}/demo.txt"
}

data "aws_vpc" "vpc-fetch" {
  filter {
    name = "tag:Team"
    values = ["Terraform"]
  }
}
data "aws_ami" "latest-ami" {
  most_recent = true
  owners = [ "amazon" ]
  filter {
    name = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*"]
  }
}

output "data"{
    value = data.local_file.foo.content
}

output "user"{
    value = data.aws_iam_users.users.names
}

output "vpc_info" {
  value = data.aws_vpc.vpc-fetch.arn
}
output "aws-ami"{
    value = data.aws_ami.latest-ami.image_id
}