data "aws_ami" "compute_ami"{
    owners = ["amazon"]
    most_recent = true
    filter {
      name = "name"
      values = [ "ubuntu/images/hvm-ssd-*/ubuntu-jammy-*" ]
    }
    filter {
      name = "architecture"
      values = ["amd64"]
    }

}

resource "aws_instance" "terra-ec2" {
  ami = data.aws_ami.compute_ami.id
  instance_type = var.instance_type
  key_name = var.key_pair
}

output "aws_ami" {
  description = "This will give me the ami id"
  value = data.aws_ami.compute_ami.id
}

