# OAuth Security Dashboard Terraform Variables

# AWS Configuration
aws_region = "us-east-1"  # Change to your preferred region

# Project Configuration
project_name = "oauth-security-dashboard"

# Cognito Configuration
cognito_domain_prefix = "oauth-sec-dash-dev-12345"  # Must be unique - change the numbers

# Application URLs (for development)
callback_urls = [
  "http://localhost:5000/auth/callback",
  "http://localhost:5001/auth/callback"
]

logout_urls = [
  "http://localhost:5000/",
  "http://localhost:5001/"
]

# RBAC Groups
create_groups = true
rbac_groups = [
  "SecurityEngineer",
  "Developer", 
  "ReadOnly"
]