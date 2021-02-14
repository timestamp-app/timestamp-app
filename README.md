# Timestamp
[![SonarCloud](https://img.shields.io/badge/Sonar-Cloud-orange)](https://sonarcloud.io/dashboard?id=timestamp-app_timestamp-app)


This project is madeup of a Azure function and a IFTTT app.

## IFTTT app
This provides a button widget on your phone that when pressed sends a json
payload to the Input function.
The json will contain the current DateTime and the Latitude/Longitude.

## Functions

### Input
The Input function takes the json from the IFTTT app, formats it, and writes
it to a table in the storage account.

It also needs a environment variable called `WIREPUSHER_ID` to make api calls
to [wirepusher](https://wirepusher.com/)

## Storage Account

### Table
The table used is called `records`.
