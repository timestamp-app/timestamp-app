const { TestScheduler } = require('jest')
const input_data = require('./mock_input.json')
const wrangler = require('../DataIngestion/data_wrangler.js')

test('formatting the timestamp', () => {
    const expected_data = {
        time: '2020/04/27 21:28',
        lat: '57.513195',
        long: '3.8307557'
    }

    wrangler.format_time(input_data)

    expect(input_data).toBe(expected_data);
});