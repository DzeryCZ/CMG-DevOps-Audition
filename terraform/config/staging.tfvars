# General
name = "cmg"
tags = {
  "Project" = "CMG"
  "Environment" = "staging"
}

# EKS
worker_node_instance_type = "t3.nano"

# Networking
vpc_cidr = "10.0.0.0/16"
private_subnets_cidrs = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
public_subnets_cidrs = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
