# Provider Block
A provider is a plugin that lets terraform manage external API
When we run terraform init, plugin required for the provider are automatically downloaded and saved locally to a .terraform directory.
whenever we give a new provider we have to run the terraform init.

# Provider Maintainers
There are 3 primary type of provider tiers in terraform
    Official - Owned and maintained by Hashicorp.
    Partner - Owned and maintained by technology company that maintains direct patnership with hashicorp.
    Community - Owned and Maintained by individual contributors.

# Provider Namespace
Namespaces are used to help users identify the organisation or publisher responsible for integration
    Official - hashicorp
    Partner - Third party organisation
    Community - Maintainers individual or organisation account

## Important
 Terraform requires explicit source information for any provider that are not hashicorp maintainer, using a new syntax in the "required_providers" nested block inside terraform configuration block.

# Resource Block
It describe one or more infrastructure objects.
A resource block declares. resource of a given type("aws_instance) - this cant be changed with a given local name this local name can be changed.
Resource type and Name together serve as an identifier for a given resource and also must be unique.

# Terraform destroy
when we want to destroy all resources we can use terraform destry
But when we want to keep one and delete another we use -target flag 
    terraform destroy -target <resource-name>.local-name

# Authentication 
we can never hardcode the secrets in the provider block.
 - The provider can source credentials and other settings from shared configuration and credential files. The issue here is every person might have a different location so hardcoding the path can create the prob.
    Default config location "$HOME/.aws/config"
 
 # Terraform State File
 Terraform stores information about managed infrastructure in a state file. The state file keeps the track of resources created by application.
   - By default the state information is stored in a file name terraform.tfstate
   - Format a state file is JSON
   - Never modify the terraform state file manually. Any mistake can cause corruption of state file.

# Desired State vs Current State
 Desired State
    Desired state is the configuration you write in your terraform files (usually ending in .tf)
    You desired state is EC2 instance of t2.micro and OS associated with it.
 Current State
    It indicates what actually exist in the real infrastructure.
 ## For example: A dev modified the instance type from t2.micro to t2.medium here the terraform file is desired state and the changed infra is current state.
 There are three phases which happens in desired and current state:
 - When you run terraform planor terraform apply , terraform first reaches out to cloud provider API to check the current state of infra
 - Terraform compares the current state(what is found in cloud) against the desired state (.tf files)
 - Based on the difference terraform determines what actions are necessary the current state match the desired state.

# Terraform refresh
The terraform refresh command check the latest state of your infra and update the state file accordingly.
 - Point - You shouldnt typically need to use this command because terraform automatically performs the same refreshing actiona as a part of creating a plan in both the terraform plan and apply commands. Its better to never use terraform refresh as it change the state file. As plan and apply command will refresh the infra state.

# Provider Versioning
Provider plugins are released seperately from terraform itself. It always better to explicitly set the provider version. For production use, you should constrain the acceptable provider versions via configurations, to ensure the new versions with breaking changes will not be automatically installed.
There are multiple ways for specifying the version of a provider
Version Number Argument                     Description
    >=1.0                                   Greater than equal to the version
    <=1.0                                   Less than Equal to the version
    ~>2.0                                   Any version in the 2.X range
    >=2.10,<=2.30                           Any version between 2.10 and 2.30

Terraform dependency lock file allows us to lock to a specific version of provider.
If a particular provider already has a selection recorded in the lock file , terraform will always re-select that version for installation, even if a newer version has become available.
If we have a terraform.lock.hcl file it maintains all the provider plugin and if you want to upgrade any plugin 
We can override with this command.
- terraform init -upgrade
