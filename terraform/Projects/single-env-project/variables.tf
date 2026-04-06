variable "project_name" {
    type = string
    description = "This is the project name"
    default = "alpha"
  
}
variable "env_name" {
    type = string
    description = "This is the project name"
    default = "prod"
  
}

variable "region"{
    type = string
    description = "This is the region in aws"
    default = "ap-south-1"
}

variable "cidr"{
    type = string
    description = "This is the cidr for aws"
    default = "10.0.0.0/24"
}
variable "subnet_public"{
    type = string
    description = "this is the public subnet range"
    default = "10.0.0.0/26"
}
variable "subnet_private"{
    type = string
    description = "this is the private subnet range"
    default = "10.0.0.64/26"
}

variable "instance_type"{
    type = string
    description = "alpha Server"
    default = "t3a.micro"
}