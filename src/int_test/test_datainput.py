import os
import unittest

import requests


class TestDataInput(unittest.TestCase):

    def setUp(self) -> None:
        if os.getenv("ENV") == 'dev':
            root_url = "https://devduck.azurewebsites.net"
        elif os.getenv("ENV") == 'prod':
            root_url = "https://wolfduck.azurewebsites.net"
        else:
            root_url = 'http://localhost:7071'

        self.url = root_url + "/api/datainput"
        self.params = {"code": os.getenv("FUNCTION_KEY")}

    def test_healthcheck(self):
        healthcheck_url = self.url + '/healthcheck'
        r = requests.get(healthcheck_url, params=self.params)
        self.assertEqual(200, r.status_code)
