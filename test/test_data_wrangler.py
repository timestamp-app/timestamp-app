import json
from unittest import TestCase

from freezegun import freeze_time
from mock import patch

from __app__.datainput import DataWrangler


class TestDataWrangler(TestCase):

    def setUp(self) -> None:
        with open(file='test/mock_input.json') as f:
            raw_input = f.read()

        input_data = json.loads(raw_input)
        self.wrangler = DataWrangler(data=input_data)

    @patch('__app__.datainput.data_wrangler.uuid4', return_value='1f83f6a2-3841-45da-8129-98de28ce7b74')
    @freeze_time("2012-01-01")
    def test_add_key_values(self, uuid4):
        expected_data = {
            'PartitionKey': '2012',
            'RowKey': '1f83f6a2-3841-45da-8129-98de28ce7b74',
            'lat': '57.513195',
            'long': '3.8307557',
            'time': 'April 27, 2020 at 09:28PM'
        }

        self.wrangler.add_key_values()

        self.assertEqual(self.wrangler.data, expected_data)

    def test_format_time(self):
        expected_data = {
            'lat': '57.513195',
            'long': '3.8307557',
            'time': '2020/04/27 21:28'
        }

        self.wrangler.format_time()

        self.assertEqual(self.wrangler.data, expected_data)
