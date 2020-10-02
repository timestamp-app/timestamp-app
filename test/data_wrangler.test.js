const fs = require('fs');

describe('wrangler tests', () => {
    let wrangler = require('../DataIngestion/data_wrangler.js')
    let input_data
    
    beforeEach(() => {
        let rawdata = fs.readFileSync('./test/mock_input.json')
        input_data = JSON.parse(rawdata)
    })
    
    test('add key values', () => {
        let expected_data = {
            PartitionKey: '2012',
            RowKey: '1f83f6a2-3841-45da-8129-98de28ce7b74',
            time: 'April 27, 2020 at 09:28PM',
            lat: '57.513195',
            long: '3.8307557'
        }
    
        wrangler.add_key_values(input_data)
    
        expect(input_data).toBe(expected_data);
    })

    test('formatting the timestamp', () => {
        let expected_data = {
            time: '2020/04/27 21:28',
            lat: '57.513195',
            long: '3.8307557'
        }
    
        wrangler.format_time(input_data)
    
        expect(input_data).toBe(expected_data);
    })
})
