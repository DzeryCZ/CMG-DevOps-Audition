# CMG Engineering Audition

## Components

- Python code of the project itself
- Terraform configuration for creating AWS infrastructure (mainly VPC and EKS)
- Dockerfiles for definition of docker images
- Helm for definition of kubernetes resources
- Gitlab-ci.yaml contains definition of pipeline

## Solution

- Configuration file is hardcoded in `./helm/cmg/templates/configmap.yaml`. When needed it can be downloaded via pipeline and replaced during deployment via `--set-file` helm option.
- Program itself works as described in documentation
- Terraform is prepared for `staging` environment and can be deployed to any AWS account
- For Pipeline there should be there CI variables properly configured in Gitlab settings
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
  - AWS_DEFAULT_REGION
  - AWS_ACCOUNT_ID
- Furthermore there should be Gitlab <> Kubernetes integration set up

## Local development

- Build Docker Image
    ```bash
    docker build -t cmg:latest -f ./docker/Dockerfile .
    ```
- Run container
    ```bash
    docker run -it -v $PWD:/var/src cmg:latest ./run.py /var/src/local/input.log
    ```
  
## AWS Setup

- Terraform
  - Go to `terraform` folder
  - Run `terraform init`
  - Run `terraform apply -var-file="./config/staging.tfvars"`
- Kubectl setup
  - Add cluster to kubectl context `aws eks --region eu-west-1 update-kubeconfig --name cmg`
- Building/Testing/Linting/Deploying in CI/CD
  - Just run defined **Gitlab** pipeline
