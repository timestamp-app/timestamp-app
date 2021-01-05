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

// Storage
resource "azurerm_storage_account" "this" {
  name                     = local.name
  resource_group_name      = azurerm_resource_group.this.name
  location                 = azurerm_resource_group.this.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

// Function
resource "azurerm_app_service_plan" "this" {
  name                = local.name
  location            = azurerm_resource_group.this.location
  resource_group_name = azurerm_resource_group.this.name
  kind                = "FunctionApp"

  sku {
    tier = "Dynamic"
    size = "Y1"
  }
}

resource "azurerm_function_app" "this" {
  name                       = local.name
  location                   = azurerm_resource_group.this.location
  resource_group_name        = azurerm_resource_group.this.name
  app_service_plan_id        = azurerm_app_service_plan.this.id
  storage_account_name       = azurerm_storage_account.this.name
  storage_account_access_key = azurerm_storage_account.this.primary_access_key
}

// DNS
resource "cloudflare_record" "cname" {
  zone_id = local.dns_zone_id
  name    = local.dns_name
  value   = azurerm_function_app.this.default_hostname
  type    = "CNAME"
  ttl     = 3600
}

resource "cloudflare_record" "txt" {
  zone_id = local.dns_zone_id
  name    = "asuid.${local.dns_name}"
  value   = azurerm_function_app.this.custom_domain_verification_id
  type    = "TXT"
  ttl     = 3600
}

resource "azurerm_app_service_custom_hostname_binding" "this" {
  depends_on = [
    cloudflare_record.cname,
    cloudflare_record.txt
  ]
  hostname            = "${local.dns_name}.treilly.co.uk"
  app_service_name    = azurerm_function_app.this.name
  resource_group_name = azurerm_resource_group.this.name
}
