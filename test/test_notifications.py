import os
from unittest import TestCase

from mock import patch, call

from helpers.notifications import push_notification


class Test(TestCase):

    def mocked_request_get(*args, **kwargs):
        return 200

    @patch("requests.get", side_effect=mocked_request_get)
    @patch.dict(os.environ, {'WIREPUSHER_ID': 'xf172'})
    def test_push_notification(self, mock_request):
        expected_data = [call('https://wirepusher.com/send',
                              params={'id': 'xf172', 'title': 'Timestamp monkey', 'message': 'hes escaped',
                                      'type': 'monkey'})]

        push_notification(code="monkey", message="hes escaped")

        self.assertEqual(expected_data, mock_request.call_args_list)
