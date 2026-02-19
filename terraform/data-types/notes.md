# Data Types
Data types refers to the type of value
Depending on the requirement, you can use wide variety of values in terraform configuration.
# Restricting Variable value to data type
 We can restrictthe value of a variable to a data type.
 variable "username"{
    type = number
 }

 Data types in terraform
    string = text
    number = numbers
    bool = either true or false
    list = a sequence of values like ["us-west-1","us-east-1"]
    set = a collection of unique values that do not have any secondary identifiers or ordering
    map = a group of values identified by named labels {name = "lable",age=33}
    null = a value that represent absence or omission

# List
Allow us to store collection of values for a single variable/argument.Useful when multiple values needs to be added to a specific argument.

# Map
A map data type represent a collection of key-value pair elements.for example it can be used with tags.

# Fetch data from list and map

var.list[2] or var.types[ap-south-1]

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

# The Count Meta Argument
By default a resource block configures one real infrastructure object. the count argument accepts a whole number and creates that many instances of the resources.
# Challenges with Count
The instances created through count and identical copies but you might want to customize certain properties for each one.