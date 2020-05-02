# Timestamp

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

In order for it to connect to the html generator function it needs to be 
provided the function key in a environment variable called `HTMLGENERATOR_KEY`.

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
