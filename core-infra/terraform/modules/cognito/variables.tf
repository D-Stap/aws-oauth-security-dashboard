variable "aws_region" {
  type        = string
  description = "AWS region for OAuth Security Dashboard Cognito resources"
}

variable "project_name" {
  type        = string
  description = "OAuth Security Dashboard project name for resource naming"
}

variable "callback_urls" {
  type        = list(string)
  description = "OAuth Security Dashboard allowed callback URLs"
}

variable "logout_urls" {
  type        = list(string)
  description = "OAuth Security Dashboard allowed logout redirect URLs"
}

variable "cognito_domain_prefix" {
  type        = string
  description = "OAuth Security Dashboard hosted UI domain prefix (must be unique in region)"
}

variable "create_groups" {
  description = "Create OAuth Security Dashboard RBAC groups"
  type        = bool
  default     = false
}

variable "rbac_groups" {
  description = "OAuth Security Dashboard RBAC groups for role-based access"
  type        = list(string)
  default     = []
}
