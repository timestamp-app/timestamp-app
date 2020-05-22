"""
This module contains the code that generates the plots and html
"""

import pandas as pd
import plotly.graph_objs as go
from jinja2 import Environment, FileSystemLoader
from plotly.offline import plot


class Generator:
    """
    This class is used to generate the plots and html
    """
    date_plot = ""

    def __init__(self, data):
        dataframe = pd.DataFrame(data)
        dataframe['time'] = pd.to_datetime(dataframe['time'], format="%Y/%m/%d %H:%M")

        self.dataframe = dataframe

    def make_plots(self):
        """
        This function makes all plots needed for the html
        :return:
        """
        self.make_date_plot()

    def make_html(self, working_directory):
        """
        This function creates a html file from a j2 template
        :param working_directory:
        :return:
        """
        file_loader = FileSystemLoader(working_directory + "/templates")
        env = Environment(loader=file_loader)
        template = env.get_template("template.html.j2")
        return template.render(plot=self.date_plot)

    def make_date_plot(self):
        """
        This function created date plots
        :return:
        """
        dataframe = self.dataframe
        dataframe['time'] = dataframe['time'].dt.date
        counts = dataframe['time'].value_counts()

        bar_plot = go.Bar(x=counts.index, y=counts.values)

        self.date_plot = plot([bar_plot], output_type="div")
