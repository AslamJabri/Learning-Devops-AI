terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = ">=6.36.0"
    }
  }
}

resource "aws_instance" "myec2" {
  ami = var.ami
  instance_type = var.instance-type
}

output "instance_id" {
  value = aws_instance.myec2.arn
}