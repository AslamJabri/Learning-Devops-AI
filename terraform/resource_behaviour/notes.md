## Resource Behaviour and Meta Argument

A resource block declares that you want a particular infrastructure object to exist with the given settings.

# How Terraform applies a Configurations

    - Create resources that exist in the configuration but are not associated with real infrastructure object in the state.
    - Destroy resources that exist in the state but no longer exist in the configuration.
    - Update in-place resources whose arguments have changed.
    - Destroy and recreate resources whose arguments have changed but which cannot be updated in-place due to remote API limitations.

# Understanding the Limitations

What happens if we want to change the default behaviour?
    - Some modification happend in real infra object that is not part of terraform but you want to ignore those changes during terraform apply.

    # Using Meta Arguments - Solution
        Terraform allows us to include meta-argument within the resource block which allow some details of this standard resourcex behaviour to be customized on a per resource basis.

# Argument and Description
**create_before_destroy**  - New replacementobject is created first, and the prior object  is destroyed after the replacement is created 

**prevent_destroy** - Terraform to reject with an error any plan that would destrou the infrastructure object assocciated with the resources.

**ignore_changes** - Ignore certain changes to the live resources that does not match the configuration.    

**replace_triggered_by** - Replaces the resource when any of the referenced items changed


## Understanding the behaviours
 **Default Behaviour**
 - By default, when terraform must change a resource argument that cannot be updated in-place due to remote API limitations, Terraform will instead destroy the existing object and then create a new replacement object with the new configured arguments.

 **Prevent Destroy**
 - This meta argument when set to true, will caise terraform to reject with an error any plan that would destroy the infrastructure object associated with the resource, as long as the argument remains present in configuration.
    - This can be used as a measure of safety against the accidental replacement of objects that may be costly to reproduce, such as db instances
    - Since this argument must be present in configuration for the protection to apply,note that this setting does not prevent the remote object from being destroyed if the resource block were removed from configuration entirely.

**Ignore Changes**
- In cases where settings of a remote object is modified by processes outside of terraform, the terraform would attempt to fix on the next run.
- In order to change this behaviour and ignore the manually applied change, we can make use of ignore_changes argument under lifecycle.
    - Instead of a list, the special keyword all may be used to instruct terraform to ignore all attributes , which means that terraform can create and destroy the remote object but will never propose updates to it.


## Resource Dependencies
 There are two ways to define dependencies in terraform.
 Explicit dependency - These are declared using the depends_on meta-argument. You use this when there's no direct attribute reference but you still need to control the order of resource creation.

 Implicit dependency - Since in aws_instance resource is a referenece of the ID of aws_security_group resource, Terraform automatically understands that the security group must be created before the EC2 instance.