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
resource "tls_private_key" "this" {
  algorithm = "ECDSA"
}

resource "tls_self_signed_cert" "this" {
  key_algorithm   = tls_private_key.this.algorithm
  private_key_pem = tls_private_key.this.private_key_pem

  validity_period_hours = 12

  early_renewal_hours = 3

  allowed_uses = [
    "key_encipherment",
    "digital_signature",
    "server_auth",
  ]

  dns_names = [
    local.dns_name_full
  ]

  subject {
    common_name  = local.dns_name_full
    organization = local.name
  }
}

resource "azurerm_app_service_certificate" "this" {
  name                = local.name
  resource_group_name = azurerm_resource_group.this.name
  location            = azurerm_resource_group.this.location
  pfx_blob            = tls_self_signed_cert.this.cert_pem
}
