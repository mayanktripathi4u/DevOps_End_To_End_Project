# Backend Config.

terraform {
  required_version = "~> 1.5"
  backend "gcs" {
    bucket = "gcp_terraform_state_files"
    prefix = "GH_TF_DevOps_E2EPrj"
  }
}