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

# Variable Definition Precedence
what if values for variable are different?
- Terraform loads variables in the following order, with later sources taking precendence over earlier ones:
1. Environment Variables
2. The terraform .tfvars file if present
3. The terraform.tfvars.json file if present
4. Any *.auto.tfvars or *.auto.tfvars.json files in lexocal order of their filenames
5. any -var and -var-file options on the command line
For example :
    if we have env variable and also the variable mentioned in .tfvar file and also we give in command line by using flag -var then it will use -var variable
    

# Local Variables
Local Values are similar to variables in a sense that it allows you to store data centrally and that can be referenced in multiple parts of configurations.

syntax: 
    locals {
        comman_tags = {
            Team = "payment-team"
        }
    }
    resource "aws_instance" "myec2"{
        ami = "sdfghjkl"
        instance_type = "t2.micro"
        tags = local.common_tags
    }

When we already have variable why do we need local variables?
 You can add expressions to locals, which allows you to complete values dynamically. Functions calls cannot be made into variables.
 Variable value can be defined in wide variety of places like terraform.tfvars,ENV,variables.CLI so on.
 Locals are more of a private resource. You have to directly modify the code.
 Local values are created by a locals block but you reference them as attributes on an object named local.