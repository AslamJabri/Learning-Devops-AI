locals {
    name_prefix = format("%s-%s", var.project_name, var.environment)
    common_tags ={
        Createdat = formatdate("DD-MMM-YY hh:mm:ss ZZZ",timestamp()),
        CreatedBy = "Terraform"
    }
}

resource "aws_vpc" "vpc_1" {
    cidr_block = var.vpc_cidr
    tags = merge(
        local.common_tags,
        {
            Name = "Terraform_VPC"
        }
    )
}

resource "aws_subnet" "public_subnet" {
  vpc_id = aws_vpc.vpc_1.id
  cidr_block = var.subnet_cidr_public
  map_public_ip_on_launch = true
  tags = merge(
    local.common_tags,{
        Name = "Public_Subnet"
    }
  )
}

resource "aws_subnet" "private_subnet"{
    vpc_id = aws_vpc.vpc_1.id
    cidr_block = var.subnet_cidr_private
    map_public_ip_on_launch = false
    tags = merge(
        local.common_tags,{
            Name = "Private_Subnet"
        }
    )
}

resource "aws_internet_gateway" "vpc_gw" {
    vpc_id = aws_vpc.vpc_1.id
    tags = merge(
        local.common_tags,{
            Name = "vpc_internet_gw"
        }
    )
}

resource "aws_route_table" "private_route" {
  vpc_id = aws_vpc.vpc_1.id
}

resource "aws_route_table" "public_route" {
  vpc_id = aws_vpc.vpc_1.id
}

resource "aws_route" "public_route" {
  route_table_id = aws_route_table.public_route.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = aws_internet_gateway.vpc_gw.id
}

resource "aws_route_table_association" "public_route" {
  subnet_id = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_route.id
}

resource "aws_route_table_association" "private_route" {
  subnet_id = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.private_route.id
}

resource "aws_security_group" "allow_ssh"{
    name= "ssh_access"
    description = "This will allow the ssh access"
    vpc_id = aws_vpc.vpc_1.id
    tags = merge(
        local.common_tags,{
            Name = "terraform_security_group"
        }
    )
}
resource "aws_vpc_security_group_ingress_rule" "ssh_rule" {
    security_group_id = aws_security_group.allow_ssh.id
    cidr_ipv4 = var.allowed_ip
    from_port = 22
    ip_protocol = "tcp"
    to_port = 22
}
resource "aws_instance" "myec2" {
    ami = var.ami_id
    instance_type = var.instance_type
    vpc_security_group_ids = [aws_security_group.allow_ssh.id]
    subnet_id = aws_subnet.public_subnet.id
    tags = local.common_tags
}