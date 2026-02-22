terraform{
    required_providers {
      aws = {
        source = "hashicorp/aws"
        
      }
    }
}
provider "aws"{
    region = "ap-south-1"
}

resource "aws_iam_user" "lb"{
    name = "terraform-user"
}

resource "aws_iam_policy" "terraform-policy"{
    name = "terraform-created-policy"
    policy = file("./policy.json")
}



resource "aws_iam_policy_attachment" "test-attach" {
  name       = "test-attachment"
  users      = [aws_iam_user.lb.name]
  policy_arn = aws_iam_policy.terraform-policy.arn
}