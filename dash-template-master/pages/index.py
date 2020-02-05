# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pickle
from pages import index, predictions, insights, process
# Imports from this application
from app import app


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## What matters matter most in a Sumo fight

            Professional Sumo's get together and fight six times a year in tournaments called Honbasho's, this is where they get a chance to rank up and climb the ladder. The rules are simple. You win, you go up. You lose, you go down; no weight class and no age groups.


            """
        ),
        dcc.Link(dbc.Button('Make a fight', color='primary'), href='/predictions')
    ],
    md=4,
)




column2 = dbc.Col(
    [
       #dcc.Graph(figure=fig)
    ]
)

layout = dbc.Row([column1, column2])

