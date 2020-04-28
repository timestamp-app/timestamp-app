import unittest

import azure.functions as func
from datainput import main

class TestFunction(unittest.TestCase):
    def test_no_json(self):
        # Construct a mock HTTP request.
        req = func.HttpRequest(
            method='POST',
            body=None,
            url='/api/datainput',
            params={})

        # Mock storage account
        storageOut = func.Out

        # Call the function.
        resp = main(req, storageOut)

        # Check the output.
        self.assertEqual(
            resp.get_body(),
            b'Requires JSON input',
        )
