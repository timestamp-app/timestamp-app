provider "azurerm" {
  features {}
}

provider "cloudflare" {}

locals {
  name        = "timestampcollector"
  dns_name    = "input.timestamp"
  dns_zone_id = "015a73c5122b5f3610eed490d5208827"
}

resource "azurerm_resource_group" "this" {
  name     = local.name
  location = "uksouth"
}
