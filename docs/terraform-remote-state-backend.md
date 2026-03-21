# Remote State Backend Setup


Apply this Terraform `remote_state_backend` before you run the main Terraform project. It will create the necessary infrastructure for the remote state backend. **Do not use the local state later in your main project**.

Use `terraform output tfstate_bucket_id` to find the bucket which will be used later for instantiating the provider block in the main project.

The remote backend uses Terraform state stored in an S3-native mechanism with `force_destroy = true` for easy cleanup, versioning enabled for state recovery, server-side encryption for security, and public access fully blocked. 

> No DynamoDB table is used for state locking; only S3 is used for state storage.

```zsh
# Go to the backend_support directory
cd remote_state_backend

# Create dev.tfvars file and fill the values there
region = 
prefix = 
environment =

# Initialize the backend_support Terraform project
terraform init

# Format Terraform files
terraform fmt

# Plan with variables
terraform plan -var-file="dev.tfvars"

# Apply changes
terraform apply -var-file="dev.tfvars"

# Show the bucket name just created
terraform output tfstate_bucket_id

# Destroy resources when done
terraform destroy -var-file="dev.tfvars"
```


#### Remote Backend Support

1. Directly specifying the backend config in the providers

```hcl

# Use the same region as you have provided in the backend directory.
# Also fetch the same tfstate_bucket_id.
# Now create the remote Terraform providers with S3 with native locking.

terraform {
  backend "s3" {
    bucket         = "<tfstate_bucket_id>"
    key            = "<state-file-path>"
    region         = "<bucket-region>"
    encrypt        = true    # Recommended for sensitive state data
    use_lockfile   = true    # Enables S3-native state locking
  }
}
```

2. With creating the backend config

```hcl
# create a backend.config with the following variables

bucket = "<tfstate_bucket_id>"
key    = "<state-file-path>"
region = "<bucket-region>"

# Initializing the project with backend config
terraform init -backend-config=backend.config
```
