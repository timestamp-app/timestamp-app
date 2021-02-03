module.exports = async function (context, req) {
    const notification = require('./notification.js')
    const wrangler = require('./data_wrangler.js')

    if (req.method == 'GET' && req.params.health == 'health') {
        // Healthcheck
        context.log.verbose('Healthcheck request recieved',);

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
        context.log.info('POST request recieved');

        wrangler.add_key_values(req.body)
        wrangler.format_time(req.body)

        notification.notify(
            context,
            'Success',
            `Record added at: ${new Date().toUTCString()}`
            )

        const response = JSON.stringify({
            status: 'Success',
            record: req.body
        })
        context.res = {
            body: response
        };
        context.log.info('POST request success');
    }
}
