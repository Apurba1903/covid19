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
age = pd.read_csv('AgeGroupDetails.csv')
cvd19 = pd.read_csv('covid_19_india.csv')

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

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH])


app.layout = html.Div([
    
    # Header
    html.Div(
        html.H1("Corona Virus Dashboard", 
                style={
                    'textAlign': 'center', 
                    'color': '#fff',
                    'padding': '20px 0 10px 0'
                }),
        style={'backgroundColor': '#2C3E50','borderRadius': '10px', 'margin': '10px' }
    ),
    
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
    html.Div([
        
        # 2nd Row First Card / Bar Chart
        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='daily-cases',
                        figure={
                            'data': [
                                go.Bar(
                                    x=cvd19['State/UnionTerritory'],
                                    y=cvd19['Confirmed'],
                                    marker=dict(
                                        color=cvd19['Confirmed'],
                                        colorscale='Viridis',
                                        showscale=True,
                                        line=dict(width=0.5, color='white')
                                ))],
                            'layout': go.Layout(
                                title='Day by Day Analysis',
                                xaxis={'title': 'State/Union Territory'},
                                yaxis={'title': 'Number of Cases'},
                                hovermode='closest',
                                plot_bgcolor='rgba(240,240,240,0.8)',
                                paper_bgcolor='rgba(240,240,240,0.5)',
                                margin={'l': 50, 'r': 20, 't': 50, 'b': 100},
                                xaxis_tickangle=-45
                            )
                        }
                    )
                ], className='card-body'),
            ], className='card', style={
                'borderRadius': '10px', 
                'margin': '10px',
                'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'
            })
        ], className='col-md-8'),
        
        # 2nd Row Second Card / Pie Chart
        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='age-pie-chart',
                        figure={
                            'data': [
                                go.Pie(
                                    labels=age['AgeGroup'],
                                    values=age['TotalCases'],
                                    hole=0.4,
                                    textinfo='label+percent',
                                    marker=dict(
                                        colors=['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0',
                                                '#9966FF', '#FF9F40', '#8AC24A', '#F7464A',
                                                '#46BFBD', '#FDB45C'],
                                        line=dict(color='#FFFFFF', width=1)
                                    ))],
                                'layout': go.Layout(
                                    title='Age Distribution of Cases',
                                    hovermode='closest',
                                    plot_bgcolor='rgba(0,0,0,0)',
                                    paper_bgcolor='rgba(0,0,0,0)',
                                    font=dict(color='#2C3E50'),
                                    legend=dict(
                                        orientation='h',
                                        yanchor='bottom',
                                        y=-0.3
                                    )
                                )
                            }
                        )
                    ], className='card-body'),
                ], className='card', style={
                    'borderRadius': '10px', 
                    'margin': '10px',
                    'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'
                })
            ], className='col-md-4') 
        
        
], className='row'),
    
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