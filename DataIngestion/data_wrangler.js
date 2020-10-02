module.exports = {
    add_key_values: function(data) {
        const uuid = require('uuid')
        data.PartitionKey = new Date().getFullYear().toString()
        data.RowKey = uuid.v4()
    },
    format_time: function(data) {
        // Was going to use ISO but azure tables detects that format and changes it
        const datetime = new Date(data.time.replace(/,|at|AM|PM/gi, ''))
        const year = datetime.getFullYear()
        const month = datetime.getMonth() + 1
        const date = datetime.getDate()
        const hour = datetime.getHours()
        const minute = datetime.getMinutes()

        data.time = `${year}/${month}/${date} ${hour}:${minute}`
    }
}