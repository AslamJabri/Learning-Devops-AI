data "aws_key_pair" "aws-key-pair"{
    key_name = "elk-training"
}


module "compute" {
  source = "./modules/compute"
  instance_type = "t3.micro"
  key_pair = data.aws_key_pair.aws-key-pair.key_name
}