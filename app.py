import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import Dash


patients = pd.read_csv('IndividualDetails.csv')

total = patients.shape[0]
active = patients[patients['current_status'] == 'Hospitalized'].shape[0]
recovered = patients[patients['current_status'] == 'Recovered'].shape[0]
deaths = patients[patients['current_status'] == 'Deceased'].shape[0]

options = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Hospitalized', 'value': 'Hospitalized'},
    {'label': 'Recovered', 'value': 'Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'}
]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    
    html.H1("Corona Virus Dashboard", style={'textAlign': 'center', 'color': '#fff'}),
    
    # First Row
    html.Div([
        
        # First Row First Card
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases", style={'textAlign': 'center', 'color': '#fff'}),
                    html.H4(total, style={'textAlign': 'center', 'color': '#fff'})
                ], className='card-body'),
            ], className='card', style={'backgroundColor': 'red', 'borderRadius': '10px', 'margin': '10px'}),            
        ], className='col-md-3'),
        
        # First Row Second Card
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases", style={'textAlign': 'center', 'color': '#fff'}),
                    html.H4(active, style={'textAlign': 'center', 'color': '#fff'})
                ], className='card-body'),
            ], className='card', style={'backgroundColor': 'blue', 'borderRadius': '10px', 'margin': '10px'}),            
        ], className='col-md-3'),
        
        # First Row Third Card
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases", style={'textAlign': 'center', 'color': '#fff'}),
                    html.H4(recovered, style={'textAlign': 'center', 'color': '#fff'})
                ], className='card-body'),
            ], className='card', style={'backgroundColor': 'orange', 'borderRadius': '10px', 'margin': '10px'}),
        ], className='col-md-3'),
        
        # First Row Fourth Card
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Deaths", style={'textAlign': 'center', 'color': '#fff'}),
                    html.H4(deaths, style={'textAlign': 'center', 'color': '#fff'})
                ], className='card-body'),
            ], className='card', style={'backgroundColor': 'green', 'borderRadius': '10px', 'margin': '10px'}),
        ], className='col-md-3')
    ], className='row'),
    
    # Second Row
    html.Div([], className='row'),
    
    # Third Row
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='dropdown',options=options,value='All'),
                    dcc.Graph(id='bar')
                ],className='card-body'),
            ],className='card', style={'borderRadius': '10px', 'margin': '10px'})
        ], className='col-md-12')
    ], className='row')
    
    
], className='container')


@app.callback(
    Output('bar', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(type):
    
    if type == 'All':
        p_bar = patients['detected_state'].value_counts().reset_index()
        return {
            'data':[go.Bar(
                    x=p_bar['detected_state'],
                    y=p_bar['count']
                )],
            'layout': go.Layout(
                title="Statewise Distribution of Patients"
            )
        }
    else:
        n_pat = patients[patients['current_status'] == type]
        p_bar = n_pat['detected_state'].value_counts().reset_index()
        return {
            'data':[go.Bar(
                    x=p_bar['detected_state'],
                    y=p_bar['count']
                )],
            'layout': go.Layout(
                title="Statewise Distribution of Patients"
            )
        }




if __name__ == '__main__':
    app.run(debug=True)