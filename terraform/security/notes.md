# Multiple Provider
There can be a requirement that multiple resources types in the same TF file need to be deployed in seperate regions.
  # Alias Meta-Argument
   Each provider can have one default configuration and any numver of alternate configurations that include an extra name segment (or alias)

# Sensitive Paramater
By default terraform will show the values associated with defined attributes in the CLI output during plan, apply operations for most of the resources.
We should design our terraform code in such a way that no sensitive information is available and shown out of the box in cli.

Adding sensitive parameter ensures that you do not accidentally exposes this data in CLI output, log output.

Note: Sensitive parameter will not protect / redact information from state file.