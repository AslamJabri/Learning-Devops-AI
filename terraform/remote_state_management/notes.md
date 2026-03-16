# Local Changes are not always good
Terraform code stored on a local machine.
 # Disadvantages
 - if laptops fails, you risk losing both your terraform and critically state file.
 - Team collabration is difficult - other members can't access or update the infrastructure code.
 - No versioning on code so no roll backs.

# Integration with GIT repo - Essential
It is very important that all of your terraform code is stored in a git repo.
NOTE: terraform.tfstate file should not be add to your git repo
    .terraform folder should not be added to your repo.


# Terraform Backends
Backends primarily determine where terraform stores its state file
When you dont specify a backend block in your terraform configuration, terraform uses the default local backend that stores terraform.tfstate in the same project folder.

# Challenges with Local Backend
    - Storing the state file locally hinders effective team collaboration.

# Recommended Architecture
- The terraform code is stored in a git repo
- The state file is stored in a central backend.

    # Supported Backends in Terraform
    - Consul
    - S3
    - azurerm
    - gcs

Accessing state in a remote service generally require some kind of credentials.
Some backends act like plain remote disk for state files; other support state locking functionality.