provider "azurerm" {
  features {}
}

provider "cloudflare" {
  api_token = var.cloudflare_token
}

provider "acme" {
  server_url = "https://acme-staging-v02.api.letsencrypt.org/directory"
}

locals {
  name           = "timestampcollector${var.env}"
  dns_name_short = "input.timestamp.${var.env}"
  dns_name_full  = "${local.dns_name_short}.treilly.co.uk"
  dns_zone_id    = "015a73c5122b5f3610eed490d5208827"

  letsencrypt_url = var.env == "prod" ? "https://acme-v02.api.letsencrypt.org/directory" : "https://acme-staging-v02.api.letsencrypt.org/directory"
}

resource "azurerm_resource_group" "this" {
  name     = local.name
  location = "uksouth"
}
