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
    html.Div([], className='row'),
    
    
], className='container')


if __name__ == '__main__':
    app.run(debug=True)