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