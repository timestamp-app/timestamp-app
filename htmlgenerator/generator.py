from plotly.offline import plot
from jinja2 import Environment, FileSystemLoader
import plotly.graph_objs as go
import pandas as pd

class generator():
    def __init__(self, data):
        df = pd.DataFrame(data)
        df['time'] = pd.to_datetime(df['time'], format="%Y/%m/%d %H:%M")

        self.df = df

    def make_html(self):
        """Creates a html file from a j2 template"""
        file_loader = FileSystemLoader("htmlgenerator/templates")
        env = Environment(loader=file_loader)
        template = env.get_template("template.html.j2")
        return template.render(plot="a plot")
        

    def date_plot(self):
        df = self.df
        df['time'] = df['time'].dt.date
        counts = df['time'].value_counts()

        bar = go.Bar(x=counts.index, y=counts.values)

        return plot([bar], output_type="div")