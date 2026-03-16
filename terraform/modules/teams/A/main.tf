provider "aws" {
  region = "ap-south-1"
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