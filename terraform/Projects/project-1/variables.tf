variable "region"{
    type = string
    description = "AWS region"
}

variable "vpc_cidr"{
    type = string
    description = "VPC cidr"
}
variable "subnet_cidr_private"{
    type = string
    description = "vpc subnet cidr"
}
variable "subnet_cidr_public"{
    type = string
}
variable "instance_type"{
    type = string
    description = "what will be the instance type"
}

variable "ami_id"{
    type = string
    description = "Instance amazon machine id"
}
variable "allowed_ip"{
    type = string
    description = "For SSH"
}
variable "project_name"{
    type = string
    description = "This is the project name"
}
variable "environment"{
    type = string
    description = "The environment we are creating"
}