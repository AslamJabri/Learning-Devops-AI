terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
    }
  }
  backend "s3" {
    bucket = "terraform-state-backend-26"
    key = "demo.tfstate"
    region = "ap-south-1"
  }
}

resource "aws_iam_user" "dev" {
  name = "terra-test-backend"
}
resource "aws_security_group" "prod" {
  name = "terraform-firewall"
}