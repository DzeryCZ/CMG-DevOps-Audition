module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = var.name
  cluster_version = "1.17"
  subnets         = [
  "subnet-062c9ec81a756883e",
  "subnet-045d559acc383e489",
  "subnet-001f1bbc15c12a081",
]

  tags = var.tags

  vpc_id = "vpc-0f01eefa0672a3f2f"

  worker_groups = [
    {
      name                          = "worker-group-1"
      instance_type                 = var.worker_node_instance_type
      asg_desired_capacity          = var.number_of_workers
      additional_security_group_ids = ["sg-06484794df3574502"]
    }
  ]

  manage_aws_auth = false
  write_kubeconfig = false
}

