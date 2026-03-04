# Challenge
Many times, the terraform plan would run properly without errors; however as soon as you run terraform apply you get an error. and this happens due to lack of validation.
Every service has some restrictions and limits on aspects like naming, convention , capacity etc.

## Terraform and Provider Validation
     The provider side validation works for many of the resources but not all of the resources. Hence it is essential to have user-side validation to ensure consistency and conformance to the standards.
## Input Variable Validation
- The input variable validation feature allows you to enforce certain rules or constraints on the values that can be assigned to input variables.
    It allows orgabisation to ensure consistency and adhere to organisational best practices.
    Allow organisations to make your terraform code more predictable.
    Allow organisation to catch misconfiguration at an early stage, saving time and potential infrastructure issues.

## Pre Conditions and Post Conditions
  **Pre-Condition**
  - Terraform preconditions are custom conditions that are checked before evaluating the object they are associated with.
  Ex: Launch EC2 instance only if it is part of free tier

  **Post_conditions**
  - Terraform post condition are custom conditions that are check after evaluating the object they are associated with.
  Ex: Verify if EC2 has Public IP address after it has been created.

# Check Blocks
the check block can validate your infrastructure outside the usual resource lifecycle.
The check block is a relatively new and powerful feature (introduced in Terraform 1.5) that allows you to perform functional validation on your infrastructure after it has been deployed.
While validation blocks (inside variables) check if your input is correct before anything happens, a check block monitors the "health" or "status" of the actual resources in the real world
**How it Works**
    A check block runs at the end of every terraform plan and terraform apply. It uses Assertions to verify that your infrastructure meets your expectations.

    Crucially, if a check fails, Terraform will not stop the deployment. It will simply show a warning. This makes it a "soft" validation tool.

# Moved Blocks
    Terraform understands moving or renaming an object as an intent to destroy the object at the old address and to create a new object at the new address.
    Using moved block, terraform treats an existing object at the old address as if it now belongs to new address.
    