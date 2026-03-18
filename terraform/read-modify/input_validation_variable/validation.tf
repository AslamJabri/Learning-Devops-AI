variable "password" {
    type = string
    description = "Password for the db"
    validation {
      condition = length(var.password) >= 12
      error_message = "Database password must be at least 12 character long"
    }
}

variable "instance_type" {}

data "aws_ec2_instance_type" "example"{
    instance_type = var.instance_type
}

resource "aws_instance" "ec2" {
  ami = "ami-1234567"
  instance_type = var.instance_type
  lifecycle {
    precondition {
      condition = data.aws_ec2_instance_type.example.free_tier_eligible
      error_message = "Please choose from the free tier only"
    }
    postcondition {
      condition = self.public_ip == ""
      error_message = "Ec2 must have Public IP"
    }
  }
}

check "health_check" {
  data "http" "web_server_status" {
    url = "https://google.com"
  }

  assert {
    condition     = data.http.web_server_status.status_code == 200
    error_message = "The web server is running, but it's not returning a 200 OK status!"
  }
}

resource "aws_security_group" "sg_group-12" {
  name = "db-sg"
}
moved {
  from = aws_security_group.sg_group-12.db-sg
  to = aws_security_group.sg_group-12.database-sg
}