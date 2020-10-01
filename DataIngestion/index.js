module.exports = async function (context, req) {
    context.log('DataIngestion function processed a request.');
    if (req.method == 'GET') {
        if (req.params.health == 'health') {
            context.res = {
                body: 'Healthy'
            };
        } else {
            context.res = {
                body: 'Invalid GET command'
            };
        }
    }
}