variable "prefix" {
  type        = string
  description = "A prefix used to name all the resources created by this configuration."
}

variable "region" {
  type        = string
  description = "The AWS region where the infrastructure will be deployed."
}

variable "github_role_suffix" {
  type        = string
  description = "Suffix for the GitHub Actions IAM role."
  default     = "github-actions-role"
}

variable "github_user" {
  type        = string
  description = "GitHub user or organization name."
}

variable "github_repo" {
  type        = string
  description = "GitHub repository name."
}

variable "github_branch" {
  type        = string
  description = "GitHub branch name."
  default     = "main"
}