terraform{
    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "6.34.0"
      }
    }
}
provider "aws"{
    region = "ap-south-1"
}

resource "aws_iam_user" "Queen-user"{
    name = "Queen"
}
resource "aws_iam_policy" "spot_instance_policy"{
    name = "spot-instance-policy"
    description = "This is the admin of spot instance"
    policy = file("policy.json")
}

resource "aws_iam_policy_attachment" "attaching_queen-ec2"{
    name = "attaching the user and policy"
    users = [aws_iam_user.Queen-user.name]
    policy_arn = aws_iam_policy.spot_instance_policy.arn
}