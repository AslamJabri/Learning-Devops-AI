resource "aws_instance" "myec2" {
    ami = "234567890"
    instance_type = "t2.micro"

    lifecycle {
      create_before_destroy = true
    }
  
}

resource "aws_instance" "myec2" {
    ami = "234567890"
    instance_type = "t2.micro"

    lifecycle {
      prevent_destroy = true
    }
  
}
resource "aws_instance" "myec2" {
    ami = "234567890"
    instance_type = "t2.micro"

    lifecycle {
        ignore_changes = [ tags ] 
    }
  
}