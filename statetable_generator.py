#generates the tables w/ data used in the state interface
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('data/floridadata.csv')

majordf = df.loc[df['Level'] == "major"]
colnames = ["Occupation_title", "Employment", "Employment_per_1000_jobs",
                      "mean_hourly_wage", "annual_mean_wage"]


fig = go.Figure(data=[go.Table(
    header=dict(values=colnames,
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[majordf.Occupation_title, majordf.Employment, majordf.Employment_per_1000_jobs,
                      majordf.mean_hourly_wage, majordf.annual_mean_wage],
               fill_color='lavender',
               align='left'))
])
fig.write_html("templates/florida.html")
