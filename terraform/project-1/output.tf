output "ec2-ip" {
  value = aws_instance.myec2.public_ip
}

output"vpc-id"{
    value = aws_vpc.vpc_1.arn
}