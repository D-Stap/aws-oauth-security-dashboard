aws_region            = "us-east-2"
project_name          = "oauth-dashboard"
cognito_domain_prefix = "dav-oauth-dashboard" # must be unique in region

callback_urls = [
  "http://localhost:5000/auth/callback",
]

logout_urls = [
  "http://localhost:5000/"
]
