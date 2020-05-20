import unittest
import json

import azure.functions as func

from datainput import main, format_input
from freezegun import freeze_time
from mock import patch


class TestMain(unittest.TestCase):
    
    # Tried mocking the azure table storage but was unable to

    def test_no_json(self):
        # Mock values
        req = func.HttpRequest(method='POST', body=None, url='/api/datainput')

        storageOut = func.Out

        # Call
        resp = main(req, storageOut)

        # Assert
        self.assertEqual(resp.get_body(), b'Requires JSON input')


class TestFormatInput(unittest.TestCase):

    @patch('datainput.uuid4', return_value='1f83f6a2-3841-45da-8129-98de28ce7b74')
    @freeze_time("2012-01-01")
    def test_ifttt_format(self, uuid4):
        # Input
        with open(file='test/mock_input.json') as f:
            raw_input = f.read()
        
        input_data = json.loads(raw_input)

        # Expected
        expected_data = {
            'PartitionKey': '2012',
            'RowKey': '1f83f6a2-3841-45da-8129-98de28ce7b74',
            'lat': '57.513195',
            'long': '3.8307557',
            'time': '2020/04/27 21:28'
        }
        
        resp = format_input(input_data)

        self.assertEqual(resp, expected_data)

