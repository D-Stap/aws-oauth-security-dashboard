output "user_pool_id" {
  value       = module.cognito.user_pool_id
  description = "OAuth Security Dashboard Cognito User Pool ID"
}

output "user_pool_client_id" {
  value       = module.cognito.user_pool_client_id
  description = "OAuth Security Dashboard Cognito App Client ID"
}

output "issuer_url" {
  value       = module.cognito.issuer_url
  description = "OAuth Security Dashboard OIDC issuer URL"
}

output "cognito_domain" {
  value       = module.cognito.cognito_domain
  description = "OAuth Security Dashboard hosted UI domain"
}
