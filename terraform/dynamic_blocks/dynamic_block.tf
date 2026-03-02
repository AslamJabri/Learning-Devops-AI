terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.34.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

variable "ports-sg" {
  type    = list(number)
  default = [22, 8000, 8001]
}

data "aws_security_group" "default-sg" {
  tags = {
    Team = "Default"
  }
}

data "aws_vpc" "default-vpc" {}

resource "aws_security_group" "main_sg" {
  name        = "dynamic-sg-example"
  description = "SG with dynamic ingress rules"
  vpc_id      = data.aws_vpc.default-vpc.id # Ensure you have this variable defined

  # THE DYNAMIC BLOCK STARTS HERE
  dynamic "ingress" {
    for_each = var.ports-sg
    
    content {
      description = "Ingress for port ${ingress.value}"
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}