import os
import unittest

import requests


class TestDataInput(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "devduck.azurewebsites.net/api/datainput"
        self.params = {"code": os.getenv("FUNCTION_KEY")}

    def test_healthcheck(self):
        r = requests.get(self.url, params=self.params)
        self.assertEqual(200, r.status_code)
