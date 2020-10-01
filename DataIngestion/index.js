module.exports = async function (context, req) {
    context.log('datainput function processed a request');
    const notification = require('./notification.js')
    const wrangler = require('./data_wrangler.js')

    if (req.method == 'GET' && req.params.health == 'health') {
        // Healthcheck
        const pjson = require('../package.json');
        const response = JSON.stringify({
            status: 'Healthy',
            version: pjson.version
        })
        context.res = {
            body: response
        };
    } else if (req.method == 'POST') {
        // Data Input
        wrangler.add_key_values(req.body)

        notification.notify(
            context, 
            'Success', 
            `Record added at: ${new Date().toUTCString()}`)
        context.res = {
            body: 'Success'
        };
    }
}