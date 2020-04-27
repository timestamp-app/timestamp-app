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

        # Call the function.
        resp = main(req)

        # Check the output.
        self.assertEqual(
            resp.get_body(),
            b'Requires JSON input',
        )
