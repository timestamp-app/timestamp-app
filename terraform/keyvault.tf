data "azurerm_client_config" "current" {}

data "azuread_service_principal" "MicrosoftWebApp" {
  application_id = "abfa0a7c-a6b6-4736-8310-5855508787cd"
}

resource "azurerm_key_vault" "this" {
  name                       = local.name
  location                   = azurerm_resource_group.this.location
  resource_group_name        = azurerm_resource_group.this.name
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  sku_name                   = "standard"
  soft_delete_enabled        = true
  soft_delete_retention_days = 7

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    certificate_permissions = [
      "create",
      "delete",
      "deleteissuers",
      "get",
      "getissuers",
      "import",
      "list",
      "listissuers",
      "managecontacts",
      "manageissuers",
      "purge",
      "setissuers",
      "update",
    ]

    key_permissions = [
      "backup",
      "create",
      "decrypt",
      "delete",
      "encrypt",
      "get",
      "import",
      "list",
      "purge",
      "recover",
      "restore",
      "sign",
      "unwrapKey",
      "update",
      "verify",
      "wrapKey",
    ]

    secret_permissions = [
      "backup",
      "delete",
      "get",
      "list",
      "purge",
      "recover",
      "restore",
      "set",
    ]
  }
  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azuread_service_principal.MicrosoftWebApp.id

    certificate_permissions = [
      "get"
    ]

    secret_permissions = [
      "get"
    ]
  }
}

resource "azurerm_key_vault_certificate" "this" {
  name         = "${local.name}-cert"
  key_vault_id = azurerm_key_vault.this.id

  certificate {
    contents = acme_certificate.certificate.certificate_p12
    password = ""
  }
  certificate_policy {
    issuer_parameters {
      name = "Self"
    }

    key_properties {
      exportable = true
      key_size   = 2048
      key_type   = "RSA"
      reuse_key  = true
    }

    secret_properties {
      content_type = "application/x-pkcs12"
    }
  }
}
