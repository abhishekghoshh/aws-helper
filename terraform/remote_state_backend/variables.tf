variable "prefix" {
  type        = string
  description = "A prefix used to name all the resources created by this configuration."
  default     = "abhishek-iac-lab"
}

variable "region" {
  type        = string
  description = "The AWS region where the infrastructure will be deployed."
  default     = "ap-south-1"
}

variable "environment" {
  type        = string
  description = "The environment where the infrastructure will be deployed."
  default     = "dev"
}