module.exports = async function (context, req) {
    const notification = require('./notification.js')
    const wrangler = require('./data_wrangler.js')

    context.log.info('POST request received');

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
