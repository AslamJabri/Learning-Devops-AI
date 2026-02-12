terraform{
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "6.32.0"
        }
    }
}
provider aws{
    region = "ap-south-1"
}

# resource "aws_eip" "elastic-ip" {
#   domain = "vpc"
# }
resource "aws_security_group" "terraform-sg" {
  name = "allow TLS from EIP"
}

resource "aws_vpc_security_group_ingress_rule" "sg-rules" {
  security_group_id = aws_security_group.terraform-sg.id
  cidr_ipv4 = "0.0.0.0/0" #this is called string interoplation
  to_port = 80
  from_port = 80
  ip_protocol = "tcp"
}


output "security_group_id"{
    value = "${aws_security_group.terraform-sg.id}"
}