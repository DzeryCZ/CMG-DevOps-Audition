data "terraform_remote_state" "networking" {
  backend = "s3"
  workspace = terraform.workspace

  config = {
    bucket = "jz-terraform-backend"
    key    = "cmg/networking.tfstate"
    region = "eu-west-1"
  }
}
