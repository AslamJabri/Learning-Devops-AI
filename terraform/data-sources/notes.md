## Data Sources

Data sources allow terraform to use/fetch defined outside of terraform.
syntax:
    data "aws_instance" "foo" {}
a data source is accessed via a special kind of resource known as data resource, declared using a data block.
Following data block requests that terraform read from a given data source ("aws_instance") and export the result under the given local name ("foo").

# Filter Structure
Within the block body (between { and }) are query constraints defined by the data source.

    data "aws_instance" "foo"{
        filter {
            name = "tag:Team"
            values = ["Production"]
        }
    }