terraform{
    required_providers {
      aws ={
        source = "hashicorp/aws"
        version = "6.32.1"
      }
    }
}

provider aws{
    region = "ap-south-1"
}

resource "aws_security_group" "allow_ssh_http" {
  name = "allow-ssh-http"
  description = "Allow ssh and HTTP on all networks"
}

resource "aws_vpc_security_group_ingress_rule" "allow-ssh" {
  security_group_id = aws_security_group.allow_ssh_http.id
  cidr_ipv4 = var.vpn_ip
  from_port = var.app_port
  to_port = var.app_port
  ip_protocol = "tcp"
}