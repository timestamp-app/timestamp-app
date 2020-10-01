module.exports = {
    add_key_values: function(data) {
        const uuid = require('uuid')
        data.PartitionKey = new Date().getFullYear()
        data.RowKey = uuid.v4()
    }
}