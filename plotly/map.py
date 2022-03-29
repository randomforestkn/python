import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.io as pio



data = pd.read_csv("WHO-COVID-19-global-data.csv")
groupby = data.groupby(' Country').max().reset_index()
groupby.head()

cases = groupby.drop(columns=[' Country_code',' Cumulative_deaths', ' WHO_region', ' New_cases', ' New_deaths'])
cases.head()

deaths = groupby.drop(columns=[' Country_code',' Cumulative_cases', ' WHO_region', ' New_cases', ' New_deaths'])
deaths.head()


casesmap = go.Figure(data = go.Choropleth(locations = cases[' Country'], z = cases[' Cumulative_cases'].astype(int), locationmode='country names', colorscale='matter', colorbar_title= 'Covid cases'))

casesmap.update_layout(title_text = "covid19 cases per country", geo=dict(showframe=False, showcoastlines=False, projection_type='equirectangular'),
                                                         annotations = [dict(x=0.5, y=0.1, text="covid cases world wide", showarrow=False)])

plot(casesmap)
