provider "aws" {
  region = "us-east-1"
}
provider "aws"{
    region= "ap-south-1"
    alias = "prod"
}
module "ec2" {
  source = "../../modules/ec2"
  ami = "ami-123"
  instance-type = "t3.micro"
}

resource "aws_eip" "myec2" {
  domain = "vpc"
  instance = module.ec2.instance_id
}
data "aws_vpc" "vpc" {
  
}
module "sg" {
  source = "../../modules/sg"
  providers = {
    aws.prod = aws.mumbai
  }
  vpc-id = data.aws_vpc.vpc.id
  security_group_name = "terraform-sg"
}

locals {
  instance_type = {
    default = "t2.nano"
    dev = "t3.micro"
    prod = "t3.small"
  }
}

resource "aws_instance" "workspace-ec2" {
  ami = "ami-1332fgh"
  instance_type = local.instance_type[terraform.workspace]
}