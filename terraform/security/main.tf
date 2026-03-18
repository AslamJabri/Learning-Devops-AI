provider "aws" {
  region = "asia-south-1"
}
provider "aws" {
  region = "us-east-1"
  alias = "usa"
}
provider "aws" {
  region = "ca-central-1"
  alias= "canada"
}


resource "aws_security_group" "prod" {
    provider = aws.canada
  name = "prod-firewall"
}

resource "aws_security_group" "staging" {
    provider = aws.usa
  name = "staging-firewall"
}


//Sensitive parameter
variable "sensitive_content" {
  sensitive = true
  default = "superpassword"
}

resource "local_file" "with_variable" {
  content = var.sensitive_content
  filename = "password.txt"
}

// we can also use localsenstive file

resource "local_sensitive_file" "variable_not_needed" {
  content = "newpassword"
  filename = "password.txt"
}