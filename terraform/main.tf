provider "azurerm" {
  features {}
}

provider "cloudflare" {}

locals {
  name           = "timestampcollector${var.env}"
  dns_name_short = "input.timestamp.${var.env}"
  dns_name_full  = "${local.dns_name_short}.treilly.co.uk"
  dns_zone_id    = "015a73c5122b5f3610eed490d5208827"
}

resource "azurerm_resource_group" "this" {
  name     = local.name
  location = "uksouth"
}
