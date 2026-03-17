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

# State Locking
Running terraform apply simultaneously by multiple team members on same project can cause terraform to make concurrent changes to the state file. This can result in state file corruption and inconsistencies.
# Introducing State Locking
State locking is a mechanism that prevents multiple operations from making concurrent changes to your infrastructure state file, which could lead to corruption or inconsistent state.
  # Process of Locking
  - Before performing any write operation, terraform attempts to acquire a "lock" on the state file.
  - If the lock is successfully acquired, terraform proceeds with the operation.
  - Once the operation is complete , terraform releases the lock allowing other processes to acquire it.

# S3 backend
The S3 backend allows terraform to store state file in a specified bucket.

# Terraform State Management

As your terraform usage becomes more advanced, there are some cases where you may need to modify the terraform state.
It is not recommended to modify the state file manually.

The terraform state command is used for advanced state management.

Sub Commands                Description
list                | List resources with in terraform state file
mv                  | Moves item with terraform state
pull                | Manually download and output the state from remote state
push                | Manually upload a loacal state file to remote state
rm                  | Removes items from terraform state
show                | Show the attributes of a single resource in the state
replace-provider    | Used to replace the provider for resources in a terraform state.


# Sub command 1 
**terraform state list** - this is used to list resources within a terraform state. Useful if you want to quickly view all resources managed by terraform.

**terraform state show** - this is used to show the attributes of a single resource in the state.

**terraform state pull** - this is used to pull the state from a remote backend and output it to stdout.

**terraform state rm** - it is used to remove items from the state. Use this when you need to remove a resource from terraform's state management without destroying it.

**terraform state mv** -  this command is used to move an item to a different address.

**terraform state replace-provider** -  this command is used to replace the provider for resources in a terraform state.

In cross project collaboration.
- The code from security team project should connect to the terraform.tfstate file managed by networking team
- The code should fetch all the IP addresses mentioned in the output values in the state file.
- The code should whitelist these IP addresses in firewall rules.

# terraform import
 Challenge
 - It can happen that all the resources in an organisation are created manually.
 - Organisation now wants to start using terraform and manage these resources via terraform.

 Solution:
 - In this terraform import can automatically create terraform configuration files for the resources you want to import.
 