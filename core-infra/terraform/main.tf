module "cognito" {
  source = "./modules/cognito"

  aws_region            = var.aws_region
  project_name          = var.project_name
  callback_urls         = var.callback_urls
  logout_urls           = var.logout_urls
  cognito_domain_prefix = var.cognito_domain_prefix
  create_groups         = var.create_groups
  rbac_groups           = var.rbac_groups
}
