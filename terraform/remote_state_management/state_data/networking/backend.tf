terraform {
  backend "s3" {
    bucket = "terraform-state-backend-26"
    key = "state-backend.tfstate"
    region ="ap-south-1"
  }
}