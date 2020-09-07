terraform {
  required_version = "=0.12.28"

  backend "s3" {
    bucket = "jz-terraform-backend"
    key    = "cmg.tfstate"
    region = "eu-west-1"
  }
}

provider "aws" {
  region  = "eu-west-1"
}
