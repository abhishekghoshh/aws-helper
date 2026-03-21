output "github_role" {
  value       = aws_iam_role.github_actions.arn
  description = "ARN of the GitHub Actions IAM role"
}
output "github_role_name" {
  value       = aws_iam_role.github_actions.name
  description = "Name of the GitHub Actions IAM role"
}
