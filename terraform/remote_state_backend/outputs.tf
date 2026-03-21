output "tfstate_bucket_id" {
  description = "The ID of the S3 bucket used for Terraform state"
  value       = aws_s3_bucket.tfstate_bucket.id
}