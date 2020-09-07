# General
variable "tags" {
  description = "Tags of created resources"
  type = map
}

variable "name" {
  description = "Name of project"
  type = string
}

# EKS
variable "worker_node_instance_type" {
  description = "Instance type of Workers"
  type = string
}

# Networking
variable "vpc_cidr" {
  description = "CIDR of VPC"
  type = string
}

variable "private_subnets_cidrs" {
  description = "List of cidrs of private subnets"
  type = list
}

variable "public_subnets_cidrs" {
  description = "List of cidrs of public subnets"
  type = list
}
