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
