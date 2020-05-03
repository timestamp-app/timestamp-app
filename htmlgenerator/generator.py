from plotly.offline import plot
from jinja2 import Environment, FileSystemLoader
import plotly.graph_objs as go
import pandas as pd
import copy

class generator():
    
    date_count_html = ""
    month_count_html = ""
    year_count_html = ""

    def __init__(self, data):
        self.df = pd.DataFrame(data)
        self.df['time'] = pd.to_datetime(
            self.df['time'],
            format="%Y/%m/%d %H:%M"
            )

    def make_plots(self):
        self.date_count_plot()
        self.month_count_plot()
        self.year_count_plot()

    def make_html(self, working_directory):
        """Creates a html file from a j2 template"""
        file_loader = FileSystemLoader(working_directory + "/templates")
        env = Environment(loader=file_loader)
        template = env.get_template("template.html.j2")
        return template.render(
            date_count_html=self.date_count_html,
            month_count_html=self.month_count_html,
            year_count_html=self.year_count_html
            )
        
    def line_plot(self, data):
        fig = go.Figure(data=go.Scatter(x=data.index, y=data.values))
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        return plot(fig, output_type="div")

    def bar_plot(self, data):
        fig = go.Figure(data=go.Bar(x=data.index, y=data.values))
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        return plot(fig, output_type="div")

    def date_count_plot(self):
        data = copy.deepcopy(self.df)
        date = data['time'].dt.date
        counts = date.value_counts().sort_index()

        self.date_count_html = self.line_plot(counts)

    def month_count_plot(self):
        data = copy.deepcopy(self.df)
        time = data['time']
        counts = time.value_counts()
        counts = counts.resample('M').sum()

        self.month_count_html = self.bar_plot(counts)

    def year_count_plot(self):
        data = copy.deepcopy(self.df)
        time = data['time']
        counts = time.value_counts()
        counts = counts.resample('Y').sum()

        self.year_count_html = self.bar_plot(counts)
