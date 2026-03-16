variable "ports" {
  type = list(number)
  default = [ 22,80,443 ]
}
variable "security_group_name" {}

variable "vpc-id" {}

resource "aws_security_group" "sg" {
  name = var.security_group_name
  vpc_id = var.vpc-id
  provider = aws.prod
  dynamic "ingress" {
    for_each = var.ports
    content {
      from_port = ingress.value
      to_port = ingress.value
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}

