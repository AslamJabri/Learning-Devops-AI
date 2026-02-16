## Variables

Repeated static values in the code can create more work in the future
    Ex: VPN IP needs to be whitelisted for 5 ports through firewall rules.

Terraform input variables are used to pass certain values from outside of the configuration.
    syntax: variable "vpn_ip"{
        default = "value"
    }
          var.vpn_ip

Benefits:
    1. Update the inportant values in one central place instead of searching and replacing them throughout your code,saving time and potential mistakes.
    2. No need to touch the core terraform configuration file.This can avoid human mistakes while editing.

# Understanding the Base
Managing variables in production environment is one of the very important aspect to keep code clean and reusable.
Hashicorp recommends a creating a seperate file with name of .tfvars to define all variables value in a project
If *.tfvar name dont start with terraform then we explicitly have to mention the tfvar file by using the flag -var-file="prod.tfvars"
# The structure would be 
1. Main terraform file which contains the code
2. Variables.tf file that defines all the variables
3. terraform.tfvars file that defines the value to all variables

When we have multiple tfvars file
    - we can specify which tfvars to take
        terraform plan -var-file="prod.tfvars"