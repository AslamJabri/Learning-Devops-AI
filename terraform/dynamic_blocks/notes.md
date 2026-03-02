# Dynamic Blocks

One of the terraform's powerful feature for keeping your code DRY (Dont Repeat Yourself) is the dynamic block.
If you have ever find yourself copy-pasting the same configuration block (like ingress rule, etc) over and over again within a single resource, Dynamic Blocks are the solution.

## Introduction Dynamic Blocks
A dynamic block allows you to generate these nested blocks programmatically based on a variable (list or map) , rather than writing them out manually.


### Terraform Taint

You have created a new resource via terraform.
Users have made a lot of manual changes (both infrastructure and inside the server)
Two ways to deal with this : Import changes to terraform /Delete and recreate the resource.
The -replace option with terraform apply to force terraform to replace an object even though there are no configuration changes that would require it.

- terraform apply -replace="aws_instance.myec2"

Points to Note
Similar kind of functionality was achieved using terraform taint command in older versions of terraform.
Form Terraform v0.15.2 and later hashicorp recommended using the -replcae option with terraform apply.