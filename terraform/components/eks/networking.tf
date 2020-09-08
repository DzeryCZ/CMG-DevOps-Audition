//data "terraform_remote_state" "networking" {
//  backend = "s3"
//
//  config = {
//    bucket = "jz-terraform-backend"
//    key    = "env:/${terraform.workspace}/cmg/networking.tfstate"
//    region = "eu-west-1"
//  }
//}