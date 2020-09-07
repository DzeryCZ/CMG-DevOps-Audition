resource "aws_ecr_repository" "cmg" {
  name                 = var.name
}

resource "aws_ecr_lifecycle_policy" "cmg" {
  repository = aws_ecr_repository.cmg.name
  policy = file("${path.module}/resources/ecr_lifecycle_policy.json")
}
