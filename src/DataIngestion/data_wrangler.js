module.exports = {
    add_key_values: function(data) {
        const uuid = require('uuid')
        data.PartitionKey = new Date().getFullYear().toString()
        data.RowKey = uuid.v4()
    },
    format_time: function(data) {
        // Was going to use ISO but azure tables detects that format and changes it
        const moment = require('moment')
        moment.locale('en')
        const datetime = moment(data.time, 'MMMM DD, YYYY at hh:mmA', true)
        data.time = datetime.format('YYYY/MM/DD HH:mm')
    }
}