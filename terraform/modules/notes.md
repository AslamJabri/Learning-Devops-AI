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
