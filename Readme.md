# CMG Engineering Audition

## Local development

- Build Docker Image
    ```bash
    docker build -t cmg:latest -f ./docker/Dockerfile .
    ```
- Run container
    ```bash
    docker run -it -v $PWD:/var/src cmg:latest /var/src/local/input.log
    ```
  
## AWS Setup

- Terraform
  - Go to `terraform` folder
  - Run `terraform init`
  - Run `terraform apply -var-file="./config/staging.tfvars"`
- Kubectl setup
  - Add cluster to kubectl context `aws eks --region eu-west-1 update-kubeconfig --name cmg`
- Building Image
  - Just run defined **Gitlab** pipeline