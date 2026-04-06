output "aws_vpc_arn"{
    description = "ARN of VPC"
    value = aws_vpc.alpha-vpc.arn
}

output "instance-ip"{
    description = "server ip"
    value = aws_instance.alpha-server.public_ip
}

output "private-key"{
    description = "private-key "
    value = tls_private_key.alpha-ec2.private_key_openssh
    sensitive = true
}