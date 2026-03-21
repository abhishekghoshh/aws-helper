# GitHub OIDC IAM Role



## Youtube

- [Securely deploy to AWS with GitHub Actions and OIDC](https://www.youtube.com/watch?v=Io5UFJlEJKc)
    - [GitHub Universe 2023 OIDC Demo](https://github.com/manchicken/ghu23-oidc-talk)
    - [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/how-tos/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)

- [How to Authenticate GitHub with AWS? | AWS IAM Role For GitHub | Terraform](https://www.youtube.com/watch?v=FICk79_6AJI)
- [How to connect GitHub workflows and AWS with OICD (OpenID Connect)](https://www.youtube.com/watch?v=aOoRaVuh8Lc)
- [AWS Hands-On: Automate AWS Infra Deployment using Terraform and GitHub Actions](https://www.youtube.com/watch?v=scecLqTeP3k)

- [Deploy AWS infrastructure using github actions and terraform](https://www.youtube.com/watch?v=j2k8UjtY4m8)
    - [gitmurali/github-actions-terraform](https://github.com/gitmurali/github-actions-terraform)

- [Deploy to AWS with Terraform within a GitHub Action](https://www.youtube.com/watch?v=GowFk_5Rx_I)
    - [CloudSecurity.dev](https://cloudsecurity.dev/)
    - [KasteM34/github-oidc-terraform](https://github.com/KasteM34/github-oidc-terraform)
    - [KasteM34/github-oidc-terraform/blob/main/github-action.yml](https://github.com/KasteM34/github-oidc-terraform/blob/main/github-action.yml)
    - [KasteM34/github-oidc-terraform/blob/main/policies/role-trusted-entity.json](https://github.com/KasteM34/github-oidc-terraform/blob/main/policies/role-trusted-entity.json)
    - [KasteM34/github-oidc-terraform/blob/main/policies/s3-bucket-state.json](https://github.com/KasteM34/github-oidc-terraform/blob/main/policies/s3-bucket-state.json)

- [GitHub Actions Pipeline for AWS with Terraform | GitHub Actions API Trigger](https://www.youtube.com/watch?v=Mm8Q8uKRjqQ)

- [Deploy to AWS with Terraform Using GitHub Actions (Secure OIDC Setup)](https://www.youtube.com/watch?v=kGJ3p1mZC3g)
    - [amir-cloud-security/terraform-test-oidc](https://github.com/amir-cloud-security/terraform-test-oidc)



## Theory

To enable secure and short-lived authentication for GitHub Actions workflows, you can create an IAM role with a trust policy for GitHub's OIDC provider. This allows your GitHub workflows to assume the role and access AWS resources without storing long-lived AWS credentials in your repository. The role should have a trust relationship with the GitHub OIDC provider and the necessary permissions for your CI/CD tasks.



## Terraform

```bash
# go to the github_role
cd github_role

# Create dev.tfvars file and fill the values there
prefix = 
region = 
github_role_suffix = 
github_user = 
github_repo = 
github_branch = 

# Initialize the backend_support Terraform project
terraform init

# Format Terraform files
terraform fmt

# Plan with variables
terraform plan -var-file="dev.tfvars"

# Apply changes
terraform apply -var-file="dev.tfvars"

# Show the github oidc role name and
terraform output github_role_name

# Destroy resources when done
terraform destroy -var-file="dev.tfvars"
```