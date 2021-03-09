# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:06:05 2021

@author: soltz
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import urllib.request
import pandas as pd
import re
from io import StringIO




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def read_data(gaugeLink):

  # Function to read data from HYDRA station for start date to end date

  # Look up URL from station ID
  

  # Read the urls  
  link = "https://or.water.usgs.gov/non-usgs/bes/{}.rain".format(gaugeLink)

  f = urllib.request.urlopen(link)

  pDat = str(f.read())

  # Split header text, header line and data
  pDat = re.split("Daily  Hourly data -->\\\\n   |-{114}\\\\n", pDat)
  
  # For the header line, insert an "H" in front of the number
  pDat = re.sub('\s+', ' H', pDat[1]) + pDat[2]

  # Fix the carriage returns
  pDat = re.sub('\\\\n', '\\n', pDat)

  pDat = StringIO(pDat)

  pDat = pd.read_csv(pDat, sep = "\s+")

  # pDat.to_csv('C:/Users/ryans/Desktop/RMS/002_projects/pdx_hydra/dash_app/data/test.csv',index = False)
  
  return(pDat)

df_gaugeInfo = pd.DataFrame({
    "Name": ["Hayden Island Rain Gauge", "Open Meadows School Rain Gauge", \
             "Shipyard Rain Gauge"],
    "Address": ["1740 N Jantzen Beach Ctr.", "7602 N Emerald Ave.", \
                "8900 N Sever Road"],
    "Link": ["hayden_island", "open_meadows", "shipyard"]
})
    
df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

availableGauges = df_gaugeInfo['Name'].unique()

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
                id='gaugeName',
                options=[{'label': i, 'value': i} for i in availableGauges],
                value=availableGauges[0]
            ),
            dcc.RadioItems(
                id='resolution',
                options=[{'label': i, 'value': i} for i in ['Hourly', 'Daily']],
                value='Daily',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '33%', 'display': 'inline-block'}),
    html.Div(children=[
        html.H4(children='Rainfall Data'),
        html.Table(id='dataTable')
        ])
    ])


@app.callback(
    Output('dataTable', 'children'),
    Input('gaugeName', 'value'),
    #Input('resolution', 'value')
    )




def generate_table(gaugeName):
    gaugeLink = df_gaugeInfo.loc[df_gaugeInfo['Name'] == gaugeName, 'Link'].iloc[0]
    rainData = read_data(gaugeLink)
    dataTable = html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in rainData.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(rainData.iloc[i][col]) for col in rainData.columns
            ]) for i in range(len(rainData))
        ])
    ])
    return dataTable


'''
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df['Year'] == year_value]

    fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                     y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                     hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig
'''

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
    