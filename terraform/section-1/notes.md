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
 - 