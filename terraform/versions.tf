terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 2.41.0"
    }
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 2.14.0"
    }
    acme = {
      source  = "vancluever/acme"
      version = "2.0.0"
    }
  }
  required_version = ">= 0.13"
}
