terraform{
    required_providers  {
        aws = {
            source = "hashicorp/aws"
            version = "6.32.0"
        }
    }
}

provider aws{
    region = "ap-south-1"
}

resource "aws_security_group" "aws-terraform-security-group"{
    name = "new-security-group"
    description = "Created by terraform for allowing port-80"
    tags = {
      Name = "Terraform-sg"
    }
}

resource "aws_vpc_security_group_ingress_rule" "allow_inbound" {
    security_group_id = aws_security_group.aws-terraform-security-group.id
    to_port = 80
    from_port = 80
    cidr_ipv4 = "0.0.0.0/0"
    ip_protocol = "tcp"
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic" {
    security_group_id = aws_security_group.aws-terraform-security-group.id
    cidr_ipv4 = "0.0.0.0/0"
    ip_protocol = -1 
}