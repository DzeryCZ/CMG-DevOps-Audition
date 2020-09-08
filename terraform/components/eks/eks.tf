module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = var.name
  cluster_version = "1.17"
  subnets         = data.terraform_remote_state.networking.outputs.private_subnets

  tags = var.tags

  vpc_id = data.terraform_remote_state.networking.outputs.vpc_id

  worker_groups = [
    {
      name                          = "worker-group-1"
      instance_type                 = var.worker_node_instance_type
      asg_desired_capacity          = var.number_of_workers
      additional_security_group_ids = [data.terraform_remote_state.networking.outputs.worker_group_mgmt_one_id]
    }
  ]

  manage_aws_auth = false
  write_kubeconfig = false
}
