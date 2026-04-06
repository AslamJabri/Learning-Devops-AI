/*Create a basic AWS infrastructure using Terraform:
VPC
Subnet
EC2 instance*/
locals {
  name = var.project_name
  env = var.env_name
  name_prefix = "${local.name}-${local.env}"
  common_tags = {
    Name    = local.name_prefix
    Env     = local.env
    Project = local.name
  }
}

data "aws_availability_zones" "az" {
  state = "available"
}
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]
}


resource "aws_vpc" "alpha-vpc" {
  cidr_block = var.cidr

  tags =  local.common_tags
  
}
resource "aws_subnet" "public_subnet" {
  vpc_id = aws_vpc.alpha-vpc.id
  cidr_block = var.subnet_public
  availability_zone = data.aws_availability_zones.az.names[0]
  map_public_ip_on_launch = true
  tags =  local.common_tags
  
}
resource "aws_subnet" "private_subnet" {
  vpc_id = aws_vpc.alpha-vpc.id
  cidr_block = var.subnet_private
  availability_zone = data.aws_availability_zones.az.names[1]
  tags = local.common_tags 
  
}

resource "aws_internet_gateway" "alpha-igw" {
  vpc_id = aws_vpc.alpha-vpc.id
  
  tags = local.common_tags
  
}

resource "aws_eip" "alpha-eip" {
  domain = "vpc"
  depends_on = [ aws_internet_gateway.alpha-igw ]
  tags = local.common_tags
  
}
resource "aws_nat_gateway" "alpha-ngw" {
  allocation_id = aws_eip.alpha-eip.id
  subnet_id = aws_subnet.public_subnet.id
  depends_on = [ aws_internet_gateway.alpha-igw ]
}

# resource "aws_internet_gateway_attachment" "alpha-igw-vpc" {
#   internet_gateway_id = aws_internet_gateway.alpha-igw.id
#   vpc_id = aws_vpc.alpha-vpc.id
# }


resource "aws_route_table" "private-route" {
  vpc_id = aws_vpc.alpha-vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.alpha-ngw.id
  }
}

resource "aws_route_table_association" "private-association" {
  subnet_id = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.private-route.id
}

resource "aws_route_table" "public-route" {
  vpc_id = aws_vpc.alpha-vpc.id
  route  {
    cidr_block= "0.0.0.0/0"
    gateway_id = aws_internet_gateway.alpha-igw.id
  }
}

resource "aws_route_table_association" "public-association" {
  subnet_id = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public-route.id
}

resource "tls_private_key" "alpha-ec2"{
    algorithm = "RSA"
    rsa_bits = 4096
}

resource "aws_key_pair" "alpha-ec2-key" {
  key_name = "${local.name}-${local.env}"
  public_key = tls_private_key.alpha-ec2.public_key_openssh
}

resource "aws_security_group" "alpha-sg" {
  name        = "allow_ssh"
  description = "Allow ssh inbound traffic and all outbound traffic"
  vpc_id      = aws_vpc.alpha-vpc.id

  tags = local.common_tags
  
}

resource "aws_security_group_rule" "alpha-sg-rule" {
  type = "ingress"
  from_port = 22
  to_port = 22
  protocol = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  security_group_id = aws_security_group.alpha-sg.id
}
resource "aws_security_group_rule" "egress_all" {
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.alpha-sg.id
}
resource "aws_instance" "alpha-server"{
    ami = data.aws_ami.ubuntu.id
    instance_type = var.instance_type
    key_name = aws_key_pair.alpha-ec2-key.id
    subnet_id = aws_subnet.public_subnet.id
    vpc_security_group_ids = [ aws_security_group.alpha-sg.id ]

    root_block_device {
      delete_on_termination = true
      volume_size = 8
      volume_type = "gp2"
    }
    tags = local.common_tags
    
}