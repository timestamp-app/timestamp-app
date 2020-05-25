import unittest

import azure.functions as func

from __app__.datainput import main


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

    def test_healthcheck(self):
        req = func.HttpRequest(method='GET',
                               body=None,
                               url='/api/datainput/healthcheck',
                               route_params={'health': 'healthcheck'})
        storageOut = func.Out

        resp = main(req, storageOut)

        # Assert
        self.assertEqual(200, resp.status_code)
