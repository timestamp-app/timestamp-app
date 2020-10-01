module.exports = {
    notify: function(context, status, message) {
        const axios = require('axios')
        const id = process.env.WIREPUSHER_ID
        const title = `Timestamp ${status}`

        axios.post(`https://wirepusher.com/send?id=${id}&title=${title}&message=${message}&type=${status}`)

        context.log('Sent notification');
    }
}