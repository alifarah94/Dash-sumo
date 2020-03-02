import dash
import pickle
#import category_encoders
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas
import os, sys
external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def load_pickle_files():
    global model
    print("Info: Step 4 - Load Pickle Files start ...")

    """ Python file containing predict function """
    with open('./pipeline2.pickle', 'rb') as f:
        model = pickle.load(f)
        

    print(model)


load_pickle_files()



app.layout = html.Div(children=[
    html.Div(
            [                                                  
                html.H1(children=' ',
                className='six columns'),
                html.Div(children='Sumo Project')
            ],className="row"),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
    
    html.Div(
            [   
                html.Div(children='Sumo1''s Age',
                className='three columns'),
           
                dcc.Slider(
                id='rikishi1_age',
                min=17,
                max=45,
                step=1,
                marks={17: '17', 20: '20', 25: '25', 30: '30', 35: '35', 40: '40', 45: '45'},
                value=17,
                className='nine columns'),
            ],className="row"),
            html.Br(),
            html.Br(),

    html.Div(
            [
                html.Div(children=' Sumo1''s Weight',
                className='three columns'),

                dcc.Slider(
                id='rikishi1_weight',
                min=80,
                max=300,
                step=5,
                marks={80: '80', 100: '100', 120: '120', 140: '140', 160: '160', 180: '180', 200: '200', 220: '220', 240: '240', 260: '260', 280: '280', 300: '300'},
                value=80,
                className='nine columns'),
            ],className="row"),
            html.Br(),
            html.Br(),

    html.Div(
            [
                html.Div(children='Sumo1''s Height',
                className='three columns'),

        dcc.Slider(
            id='rikishi1_height',
            min=160,
            max=210,
            step=1,
            marks={160: '160', 165: '165', 170: '170', 175: '175', 180: '180', 185: '185', 190: '190', 195: '195',200: '200', 205: '205', 210: '210'},
            value=160,
            className='nine columns'),
            ],className="row"),
            html.Br(),
            html.Br(),

    html.Div(
            [
                html.Div(children='Sumo1''s Heya',
                className='three columns'),

        dcc.Dropdown(
        id='rikishi1_heya',
        options=[
            {'label': 'Sadogatake', 'value': 'Sadogatake'},
            {'label': 'Futagoyama', 'value': 'Futagoyama'},
            {'label': 'Kasugano', 'value': 'Kasugano'},
            {'label': 'Dewanoumi', 'value': 'Dewanoumi'},
            {'label': 'Kokonoe', 'value': 'Kokonoe'},
            {'label': 'Tokitsukaze', 'value': 'Tokitsukaze'},
            {'label': 'Takasago', 'value': 'Takasago'},
            {'label': 'Izutsu', 'value': 'Izutsu'},
            {'label': 'Musashigawa', 'value': 'Musashigawa'},
            {'label': 'Kataonami', 'value': 'Kataonami'}
        ], value = 'Sadogatake',className='nine columns'),
            ],className="row"),

            html.Br(),
            html.Br(),

    html.Div(
            [
                html.Div(children='Sumo1''s Shusshin',
                className='three columns'),

            dcc.Dropdown(
            id='rikishi1_shusshin',
            options=[
                {'label': 'Mongolia', 'value': 'Mongolia'},
                {'label': 'Aomori', 'value': 'Aomori'},
                {'label': 'Kagoshima', 'value': 'Kagoshima'},
                {'label': 'Tokyo', 'value': 'Tokyo'},
                {'label': 'Chiba', 'value': 'Chiba'},
                {'label': 'Fukuoka', 'value': 'Fukuoka'},
                {'label': 'Ibaraki', 'value': 'Ibaraki'},
                {'label': 'Hokkaido', 'value': 'Hokkaido'},
                {'label': 'Hyogo', 'value': 'Hyogo'},
                {'label': 'U.S.A.', 'value': 'U.S.A.'}
            ], value='Mongolia',className='nine columns'),

            ],className="row"),
            html.Br(),
            html.Br(),
            html.Br(),
             html.Div(id='output'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

    html.Div(
            [   
                html.Div(children='Sumo2''s Age',
                className='three columns'),
           
                dcc.Slider(
                id='rikishi2_age',
                min=17,
                max=45,
                step=1,
                marks={17: '17', 20: '20', 25: '25', 30: '30', 35: '35', 40: '40', 45: '45'},
                value=17,
                className='nine columns'),
            ],className="row"),
            html.Br(),
            html.Br(),

    html.Div(
            [
                html.Div(children=' Sumo2''s Weight',
                className='three columns'),

                dcc.Slider(
                id='rikishi2_weight',
                min=80,
                max=300,
                step=5,
                marks={80: '80', 100: '100', 120: '120', 140: '140', 160: '160', 180: '180', 200: '200', 220: '220', 240: '240', 260: '260', 280: '280', 300: '300'},
                value=80,
                className='nine columns'),
            ],className="row"),
            html.Br(),
            html.Br(),

    html.Div(
            [
                html.Div(children='Sumo2''s Height',
                className='three columns'),

        dcc.Slider(
            id='rikishi2_height',
            min=160,
            max=210,
            step=1,
            marks={160: '160', 165: '165', 170: '170', 175: '175', 180: '180', 185: '185', 190: '190', 195: '195',200: '200', 205: '205', 210: '210'},
            value=160,
            className='nine columns'),
            ],className="row"),
            html.Br(),
            html.Br(),

    html.Div(
            [
                html.Div(children='Sumo2''s Heya',
                className='three columns'),

        dcc.Dropdown(
        id='rikishi2_heya',
        options=[
            {'label': 'Sadogatake', 'value': 'Sadogatake'},
            {'label': 'Futagoyama', 'value': 'Futagoyama'},
            {'label': 'Kasugano', 'value': 'Kasugano'},
            {'label': 'Dewanoumi', 'value': 'Dewanoumi'},
            {'label': 'Kokonoe', 'value': 'Kokonoe'},
            {'label': 'Tokitsukaze', 'value': 'Tokitsukaze'},
            {'label': 'Takasago', 'value': 'Takasago'},
            {'label': 'Izutsu', 'value': 'Izutsu'},
            {'label': 'Musashigawa', 'value': 'Musashigawa'},
            {'label': 'Kataonami', 'value': 'Kataonami'}
        ], value = 'Sadogatake',className='nine columns'),
            ],className="row"),

            html.Br(),
            html.Br(),

    html.Div(
            [
                html.Div(children='Sumo2''s Shusshin',
                className='three columns'),

            dcc.Dropdown(
            id='rikishi2_shusshin',
            options=[
                {'label': 'Mongolia', 'value': 'Mongolia'},
                {'label': 'Aomori', 'value': 'Aomori'},
                {'label': 'Kagoshima', 'value': 'Kagoshima'},
                {'label': 'Tokyo', 'value': 'Tokyo'},
                {'label': 'Chiba', 'value': 'Chiba'},
                {'label': 'Fukuoka', 'value': 'Fukuoka'},
                {'label': 'Ibaraki', 'value': 'Ibaraki'},
                {'label': 'Hokkaido', 'value': 'Hokkaido'},
                {'label': 'Hyogo', 'value': 'Hyogo'},
                {'label': 'U.S.A.', 'value': 'U.S.A.'}
            ], value='Mongolia',className='nine columns'),

            ],className="row")








])



@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='rikishi1_age', component_property='value')])
def update_value(input_data):
    return input_data









if __name__ == '__main__':
    app.run_server(debug=True)
