// DNS
resource "cloudflare_record" "cname" {
  zone_id = local.dns_zone_id
  name    = local.dns_name_short
  value   = azurerm_function_app.this.default_hostname
  type    = "CNAME"
  ttl     = 3600
}

resource "cloudflare_record" "txt" {
  zone_id = local.dns_zone_id
  name    = "asuid.${local.dns_name_short}"
  value   = azurerm_function_app.this.custom_domain_verification_id
  type    = "TXT"
  ttl     = 3600
}

resource "azurerm_app_service_custom_hostname_binding" "this" {
  depends_on = [
    cloudflare_record.cname,
    cloudflare_record.txt
  ]
  hostname            = local.dns_name_full
  app_service_name    = azurerm_function_app.this.name
  resource_group_name = azurerm_resource_group.this.name
}

// Cert
resource "azurerm_app_service_certificate" "this" {
  name                = local.name
  resource_group_name = azurerm_resource_group.this.name
  location            = azurerm_resource_group.this.location
  key_vault_secret_id = azurerm_key_vault_certificate.this.id
}

resource "azurerm_app_service_certificate_binding" "this" {
  hostname_binding_id = azurerm_app_service_custom_hostname_binding.this.id
  certificate_id      = azurerm_app_service_certificate.this.id
  ssl_state           = "SniEnabled"
}
