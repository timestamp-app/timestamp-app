"""
This module is responsible for formatting and writing the input data
"""

import json
from datetime import datetime
from uuid import uuid4


class DataWrangler:
    """
    This class formats and writes the data
    """

    def __init__(self, data):
        self.data = data

    def add_key_values(self):
        """
        This function adds a partition and row key for the azure table
        :return:
        """
        self.data["PartitionKey"] = str(datetime.today().year)
        self.data["RowKey"] = str(uuid4())

    def format_time(self):
        """
        This function formats the time from the format IFTTT uses to our preferred one
        :return:
        """
        ifttt_time_fmt = "%B %d, %Y at %I:%M%p"
        # Was going to use ISO but azure tables detects that format and changes it
        preferred_time_fmt = "%Y/%m/%d %H:%M"
        datetime_obj = datetime.strptime(self.data["time"], ifttt_time_fmt)
        self.data["time"] = datetime_obj.strftime(preferred_time_fmt)

    def write_to_table(self, table):
        """
        This function writes the data to a azure table
        :param table: The table object to write to
        :return:
        """
        table.set(json.dumps(self.data))
