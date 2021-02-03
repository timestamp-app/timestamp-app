# Timestamp
[![TerraformCloud](https://img.shields.io/badge/Terraform-Cloud-blue)](https://app.terraform.io/app/timestamp-app/workspaces/timestamp-app/runs)
[![SonarCloud](https://img.shields.io/badge/Sonar-Cloud-orange)](https://sonarcloud.io/project/configuration?id=treilly94_timestamp-app)


This project is madeup of two Azure functions and a IFTTT app.
It also generates a static website that can be hosted by from a azure storage
account.

## IFTTT app
This provides a button widget on your phone that when pressed sends a json
payload to the datainput function.
The json will contain the current date/time and the latitude/longatude.

## Functions

### DataInput function
The datainput function takes the json from the IFTTT app, formats it, and writes
it to a table in the storage account.
It will then trigger the generatehtml function.

It also needs a environment variable called `WIREPUSHER_ID` to make api calls
to [wirepusher](https://wirepusher.com/)

### HTMLGenerator function
The html generator function reads from the table in the storage account,
generates some graphs and statistics, and writes them in the form of a html file
to a blobstore in the storage account. The storage account will then host a
static website ontop.

## Storage Account

### Table
The table used is called `records`. if it douesnt exist beforehand it will be
created.

### Static Website
At the minute this must be created manually in the storage account beforehand.
Steps:
1. If its not already ensure the storage account is running `v2`
2. Enable `Static Website` in the static website tab.
3. Set `Index document name` to `index.html`

This will create a `$web` container and setup a static website. Once run the
html generator function will generate the index.html document and drop in the
`$web` container.
