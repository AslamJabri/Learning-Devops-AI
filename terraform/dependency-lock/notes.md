## Ephemeral Blocks
The ephemeral block defines resources that are essentially temporary.
Ephemeral resources have a unique lifecycle, and terraform does not store information about ephemeral resources in state or plan files.

To use write only arguments youmust use terraform v1.11 or later and use a resource that supports write only arguments.

write only arguments accept both ephemeral and non-ephemeral values.

terraform does not store write only arguments in state files so terraform has no way of knowing if a write only argument value has changed.

Terraform also cannot create plan diffs for write-only arguments because it does not store those values in plan files.

Providers typically include version arguments alongside write-only arguments. Terraform stores version arguments in state and can track if a version argument changes.

## Trigger an update

To trigger an update of write-only argument, increment the version argument's value in your configuration.
When you increment the password_wo_version argument, Terraform notices that change in its plan and notifies the aws provider. The aws provider then uses the new password_wo valur to update the aws_db_instance resource.

The implementation of write only arguments and their version argumnts is provider specific.