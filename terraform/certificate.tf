resource "tls_private_key" "private_key" {
  algorithm = "RSA"
}

resource "acme_registration" "reg" {
  account_key_pem = tls_private_key.private_key.private_key_pem
  email_address   = "treilly94@live.com"
}

resource "acme_certificate" "certificate" {
  account_key_pem = acme_registration.reg.account_key_pem
  common_name     = local.dns_name_full
  #   subject_alternative_names = ["www2.example.com"]

  dns_challenge {
    provider = "cloudflare"
  }
}
