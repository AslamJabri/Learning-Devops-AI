In software engineering dont repeat yourself is a principle of aoftware development aimed at reducing repetition of software patterns.

The devops team can create the template in central location that all can use.

## Introducing terraform modules

Terraform modules allows us to centralise the resoure configuration and it makes it easier for multiple projects to re-use  the terraform code for projects.
Instead of writing code form scratch we can use multiple ready-made modules

Terraform registry can contain multiple modules for aspecific infrastructure resource maintained by different users.

## Creating Base Module Structure
A base "modules" folder.
A sub-folder containing name for each modules that are available.
Each modules sub folder contains the actua module terraform code that other projects can reference from.
Each team can call various set of modules that are available in the modules folder based on their requirement.

# Challenges
    # Hardcoded values
        The values are hardcoded as part of the module
        if developer is calling the module, he will have to stick with same values.
        Developer will not be able to override the hardcoded values of the module.

    -- Convert hard coded values to variables
        For modules it is especially recommended to convert ahrd-coded values to variables.so that it can be overridden based on user requirement.
    
    ## Provider Improvements
     Avoid hard coding in the module as much as possible
     A required_provider block with version constraints for module to work is imp.

     The required block is imp in module is because it could be possible the version can be there.

# Output Values
output values make information about your infrastructure available on the cli and can expose information for other terraform configurations to use.

# Accessing Child Module Outputs
Ensure to include output values in the module code for better flexibility and integration with other resources and projects.
Format : module.<MODULE NAME>.<OUTPUT NAME>


# Root and Child Modules

Root module reside in the main working directory of your terraform configuration. This is the entry point for your infrastructure definition

Child module that has been called by another module is often referred to as child module.

# Standard Module Structure
The standard module structure is a file and directory layout hashicorp recommends for reusable modules.
A minimal recommended module following the standard structure is shown below
  $ directory 
    |-- README.md
    |-- main.tf
    |-- variables.tf
    |-- outputs.tf
# Scope the requirements for module creation
- A team wants to provision their infrastructure using terraform.
- Architecture diagram depicts the desired outcome.
- In this scenario, a team of terraform producers who write terraform code from scratch, will build a collection of modules to provision the infrastructure and applications.
- The members of the team in charge of the application will consume these modules to provision the infrastructure they need.
- After reviewing the consumers team's requirement the producer team has broken up the application infrastructure into following modules:
- Network, Web, App, Database, Routing and Security.

# Multiple Provider blocks

when we have two security groups one for dev which should come in us-east-1 and other one prod which should come in mumbai then how can we handle this.
- Passing Providers Explicitly
    You can use provider argument within a module block to explicitly define which provider configurations are available to the chile module.

- In the child module you need to also declare the configuration aliases for the provider.
- you can use provider meta-argument within resource to choose appropriate provider configuration.

# Terraform Workspace
- Can we have multiple state file for single terraform configuration?
- Can we manage different env's through it seperately.
 For achieving this we can make use of terraform workspace
 - It enables us to manage multiple set of deployments from the same set of configuration file.
 - each workspace will have there own tfstate file.

 commands:
  To list the workspaces - terraform workspace list
  Switch to another workspace - terraform workspace select dev
  create new workspace - terraform workspace new <workspace name>
  show the current workspace - terraform workspace show <workspace name>
  delete the workspace - terraform workspace delete <workspace name>
