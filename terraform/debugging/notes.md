## Terraform Debugging
Terraform has detailed logs that you can enable by setting the TF_LOG environment variable to any value.
You can set TF_LOG to one of the log levels. (in order of decreasing verbosity)

Log Level
    Trace
    Debug
    INFO
    Warn
    Error

## To Persist the Logs
To persist logged output you can set TF_LOG_PATH in order to force the log to always be appended to a specific file when logging is enabled.

export TF_LOG=INFO
export TF_LOG_PATH=terraform.txt

# Terraform Troubleshooting Model

There are four potential types of issues that you could experience with terraform.
- Language, State, Core and Provider Errors.

- Language: In most of the cases, the errors that you will face will be related to this. When terraform encounters a syntax error in your configuration, it prints out the line numbers and an explanation of the error.
- State:  if state is out of sync , terraform may destroy or change your existing resources. If state is locked , you will alse be blocked from running write operations.
- Core: These errors are directly related to the main application. Errors produced at this level may be a bug.
- Provider: These set of errors are primarily related to the provider plugins. Use provider github page to report the bug on the plugin.

### Importance of Readibility
When multiple engineers work on the same codebase, varying code styles can make code reviews painful and debugging difficult.
The terraform fmt command formats terraform configuration file contents so that it matches the cacocical format and style.
- terraform fmt

If you want to see exactly what terraform fmt is changing , use -diff flag.
- terraform fmt -diff

# Recursive Formatting
By default terraform fmt only looks at the current directory.if you have complex project with subdirectories use the -recursive flag
- terraform fmt -recursive

# Check Mode
In CI/CD pipelines you often want to verify if the code is formatted correctly without actually modifying it. The -check flag return 0 if all files are formatted correctly and 3 if any file require formatting.
- terraform fmt -check

Point to Note:
    Terraform fmt does not change the behaviour of your infrastructure it only changes how the code looks. 


### Load order and Semantics
Terraform normally loads all of the .tf and .tf.json files within a directory. The files loaded must end in either .tf or .tf.json.
----- # Points to Note
  -  Since terraform loads all of the .tf and .tf.json files within the directory, it expects each one to define a distinct set of configuration objects. If two files attempt to define the same object terraform returns error.
  -  Terraform loads all configuration files within the directory specified in alphabetical order.
  - Terraform does not automatically read sub directories unless explicitly called.