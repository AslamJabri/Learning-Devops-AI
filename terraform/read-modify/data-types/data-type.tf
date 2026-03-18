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
    instance_type = var.list[count.index]
    count = 2

    tags = {
        Name = "payment-system-${count.index}"
    }
}

# Conditionals

variable "environment"{
    default = "development"
}
resource "aws_instance" "conditional_example"{
    ami = "ami-342"
    instance_type = var.environment == "development" ? "t2.micro" : "t3a.small"  
}

# Conditional expression with multiple values
variable "environment-new" {
    default = "development"
}
variable "region" {
    default = "ap-south-1"
}

resource "aws_instance" "conditional-multiple-values"{
    ami = "ami-134567"
    instance_type = var.environment-new == "development" && var.region == "ap-south-1" ? "t2.micro" : "t2.small"
}