provider aws {}

variable "list" {
    type = list
    default = ["m5.large","m5.xlarge","t3a.medium"]
}
variable "types"{
    type = map
    default = {
        ap-south-1 = "t2.micro"
        us-east-1 = "t3a.medium"
        us-west-1 = "t2.nano"
    }
}

resource "aws_instance" "ec2" {
    ami = "ami-123"
    instance_type = var.list[2]
    count = 2
}