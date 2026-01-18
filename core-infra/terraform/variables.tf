variable "aws_region" {
  description = "AWS region for OAuth Security Dashboard deployment"
  type        = string
  default     = "us-east-2"
}

variable "project_name" {
  description = "OAuth Security Dashboard project identifier"
  type        = string
  default     = "identity-dashboard"
}

variable "callback_urls" {
  description = "OAuth Security Dashboard callback URLs for authentication"
  type        = list(string)
  default     = ["http://localhost:5000/auth/callback"]
}

variable "logout_urls" {
  description = "OAuth Security Dashboard logout redirect URLs"
  type        = list(string)
  default     = ["http://localhost:5000/"]
}

variable "cognito_domain_prefix" {
  description = "OAuth Security Dashboard Cognito hosted UI domain prefix"
  type        = string
  default     = "identity-dashboard-dev"
}

variable "create_groups" {
  description = "Create OAuth Security Dashboard RBAC groups in Cognito user pool"
  type        = bool
  default     = true
}

variable "rbac_groups" {
  description = "OAuth Security Dashboard role-based access control groups"
  type        = list(string)
  default     = ["SecurityEngineer", "Developer"]
}
