provider "aws" {
  region     = "ap-south-1"
  access_key = "$access_key"
  secret_key = "$secret_access_key"
}

resource "aws_instance" "terraform_ec2" {
  ami           = "ami-0ff5003538b60d5ec"
  instance_type = "t3.micro"
  tags = {
    Name = "Terraform_created_ec2"
  }
}