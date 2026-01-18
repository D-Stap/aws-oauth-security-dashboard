output "user_pool_id" {
  value       = aws_cognito_user_pool.this.id
  description = "OAuth Security Dashboard Cognito User Pool ID"
}

output "user_pool_client_id" {
  value       = aws_cognito_user_pool_client.this.id
  description = "OAuth Security Dashboard Cognito App Client ID"
}

output "issuer_url" {
  value       = "https://cognito-idp.${var.aws_region}.amazonaws.com/${aws_cognito_user_pool.this.id}"
  description = "OAuth Security Dashboard OIDC Issuer URL"
}

output "cognito_domain" {
  value       = "https://${aws_cognito_user_pool_domain.this.domain}.auth.${var.aws_region}.amazoncognito.com"
  description = "OAuth Security Dashboard Cognito Hosted UI domain"
}
