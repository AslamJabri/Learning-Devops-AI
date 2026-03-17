resource "aws_security_group" "allow_tls" {
  name = "allow_tls"
}

data "terraform_remote_state" "vpc"{
    backend = "s3"
    config = {
      bucket = "terraform-state-backend-26"
      key = "state-backend.tfstate"
      region ="ap-south-1"
    }
}

resource "aws_vpc_security_group_ingress_rule" "allow_tls_ipv4" {
  security_group_id = aws_security_group.allow_tls.id
  cidr_ipv4 = "${data.terraform_remote_state.vpc.outputs.eip_addr}/32"
  from_port = 22
  to_port = 22
  ip_protocol = "tcp"
}