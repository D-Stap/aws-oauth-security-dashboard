locals {
  user_pool_name = "${var.project_name}-user-pool"
  client_name    = "${var.project_name}-app-client"
}

resource "aws_cognito_user_pool" "this" {
  name = local.user_pool_name

  username_attributes = ["email"]

  auto_verified_attributes = ["email"]

  password_policy {
    minimum_length                   = 12
    require_lowercase                = true
    require_uppercase                = true
    require_numbers                  = true
    require_symbols                  = false
    temporary_password_validity_days = 7
  }

  account_recovery_setting {
    recovery_mechanism {
      name     = "verified_email"
      priority = 1
    }
  }

  admin_create_user_config {
    allow_admin_create_user_only = true
  }

  mfa_configuration = "OFF"

  # Email attribute for OAuth Security Dashboard authentication
  schema {
    attribute_data_type      = "String"
    name                     = "email"
    required                 = true
    mutable                  = true
    developer_only_attribute = false
    string_attribute_constraints {
      min_length = "5"
      max_length = "256"
    }
  }

  tags = {
    Project = var.project_name
    Env     = "dev"
  }
}

resource "aws_cognito_user_pool_client" "this" {
  name         = local.client_name
  user_pool_id = aws_cognito_user_pool.this.id

  # Public client using Authorization Code Flow with PKCE
  generate_secret = false

  supported_identity_providers = ["COGNITO"]

  allowed_oauth_flows = ["code"]
  allowed_oauth_scopes = [
    "openid",
    "email",
    "profile"
  ]
  allowed_oauth_flows_user_pool_client = true

  callback_urls = var.callback_urls
  logout_urls   = var.logout_urls

  prevent_user_existence_errors = "ENABLED"

  explicit_auth_flows = [
    "ALLOW_USER_SRP_AUTH",
    "ALLOW_REFRESH_TOKEN_AUTH",
    "ALLOW_USER_PASSWORD_AUTH"
  ]

  access_token_validity  = 60
  id_token_validity      = 60
  refresh_token_validity = 12
  token_validity_units {
    access_token  = "minutes"
    id_token      = "minutes"
    refresh_token = "hours"
  }
}

resource "aws_cognito_user_pool_domain" "this" {
  domain       = var.cognito_domain_prefix
  user_pool_id = aws_cognito_user_pool.this.id
}

# Security Dashboard access control groups
resource "aws_cognito_user_group" "rbac" {
  count        = var.create_groups ? length(var.rbac_groups) : 0
  name         = var.rbac_groups[count.index]
  user_pool_id = aws_cognito_user_pool.this.id
  description  = "OAuth Security Dashboard ${var.rbac_groups[count.index]} access group"
}
