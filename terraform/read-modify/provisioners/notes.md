# Terraform Provisioners

We have been using Terraform to create and manage resources for specific provider.
Organizations would want end to end solution for creation of infrastructure and configuring appropriate packages required for the application.
- Provisioners are used to execute scripts on a local or remote machine as part of resource creation or destruction
Ex: For installing the software packages.

# Types of Provisioners

local-exec
remote-exec

# Local-exec provisioner
The local-exec provisioner invokes a local executable after a resource is created.
Ex: After Ec2 is launched fetch the IP and store it in file server_ip.txt

# Remote-exec provisioner
 remote-exec provisioner allow to invoke scripts or run commands directly on the remote server.
 Ex: After Ec2 is launched install apache software.

 ## Syntax:
   resource "aws_instance" "myec2"{
    ami = "ami-4567"
    instance_type = "t2.micro"

    connection {
        type = "ssh"
        user = "ec2-user"
        private_key = file("./key.pem")
        host = self.public_ip
    }

    provisioner "local-exec" {
        command = "echo server has been created through terraform"

    }

    provisioner "remote-exec" {
        inline = {
            "sudo yum install -y nginx",
            "sudo systemctl start nginx"
        }
    }
   }