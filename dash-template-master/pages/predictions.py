# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import assets
import os, sys
from joblib import load
import pandas

# Imports from this application

import pickle


#THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
#print(THIS_FOLDER)
#my_file = os.path.join(THIS_FOLDER, 'pipeline.sav')
#print(my_file)
#print(os.getcwd())
#model = 'pipeline.sav'
#loaded_model = pickle.load(open(my_file, 'rb'))
#loaded_model = pickle.load(open('assests/pipeline.sav', 'rb'))
#load('Documents/dash-template-master/pages/pipeline.joblib')

#pipeline = pickle.load(open('assets/pipeline.sav', 'rb'))
#pickle.dump(pipeline, open('pipeline.sav', 'wb'))

def load_pickle_files():
    global model
    print("Info: Step 4 - Load Pickle Files start ...")

    """ Python file containing predict function """
    with open('./pipeline2.pickle', 'rb') as f:
        model = pickle.load(f)

    print("Info: Load Pickle Files completed ...")


load_pickle_files()


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(

        ),

            dcc.Markdown("",id='sumo1_age',className='mb-1'),
            dcc.Markdown("",id='sumo1_weight',className='mb-1'),
            dcc.Markdown("",id='sumo1_height',className='mb-1'),
            dcc.Markdown("",id='sumo1_heya',className='mb-1'),
            dcc.Markdown("",id='sumo1_shussin',className='mb-5'),
            dcc.Markdown("",id='sumo2_age',className='mb-1'),
            dcc.Markdown("",id='sumo2_weight',className='mb-1'),
            dcc.Markdown("",id='sumo2_height',className='mb-1'),
            dcc.Markdown("",id='sumo2_heya',className='mb-1'),
            dcc.Markdown("",id='sumo2_shussin',className='mb-5'), dcc.Markdown("",id='prediction-content'),
    ],
    md=4,
)

column2 = dbc.Col(
    [   dcc.Markdown(" # Make your sumo",className='mb-5'),
        dcc.Slider(
            id='rikishi1_age',
            min=17,
            max=45,
            step=1,
            marks={17: '17', 20: '20', 25: '25', 30: '30', 35: '35', 40: '40', 45: '45'},
            # {i: '{}'.format(i*2) for i in range(20)},
            value=17,
            className='mb-5'

        ),
        # text below slider

            dcc.Slider(
            id='rikishi1_weight',
            min=80,
            max=300,
            step=5,
            marks={80: '80', 100: '100', 120: '120', 140: '140', 160: '160', 180: '180', 200: '200', 220: '220', 240: '240', 260: '260', 280: '280', 300: '300'},
            # {i: '{}'.format(i*2) for i in range(20)},
            value=80,
            className='mb-5'

        ),
        dcc.Slider(
            id='rikishi1_height',
            min=160,
            max=210,
            step=1,
            marks={160: '160', 165: '165', 170: '170', 175: '175', 180: '180', 185: '185', 190: '190', 195: '195',
                   200: '200', 205: '205', 210: '210'},
            # {i: '{}'.format(i*2) for i in range(20)},
            value=160,
            className='mb-5'

        ),
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
        ], value = 'Sadogatake',className='mb-5'),
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
            ], value='Mongolia',className='mb-5'), dcc.Markdown(" # Enemy Sumo", className='mb-5'),dcc.Markdown("",className='mb-5'),

            dcc.Slider(
            id='rikishi2_age',
            min=17,
            max=45,
            step=1,
            marks={17: '17', 20: '20', 25: '25', 30: '30', 35: '35', 40: '40', 45: '45'},
            # {i: '{}'.format(i*2) for i in range(20)},
            value=17,
            className='mb-5'

        ),
        # text below slider

            dcc.Slider(
            id='rikishi2_weight',
            min=80,
            max=300,
            step=5,
            marks={80: '80', 100: '100', 120: '120', 140: '140', 160: '160', 180: '180', 200: '200', 220: '220', 240: '240', 260: '260', 280: '280', 300: '300'},
            # {i: '{}'.format(i*2) for i in range(20)},
            value=80,
            className='mb-5'

        ),
        dcc.Slider(
            id='rikishi2_height',
            min=160,
            max=210,
            step=1,
            marks={160: '160', 165: '165', 170: '170', 175: '175', 180: '180', 185: '185', 190: '190', 195: '195',
                   200: '200', 205: '205', 210: '210'},
            # {i: '{}'.format(i*2) for i in range(20)},
            value=160,
            className='mb-5'

        ),
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
        ], value = 'Sadogatake',className='mb-5'),
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
            ], value='Mongolia',className='mb-5'),

    ]
)

layout = dbc.Row([column1, column2])


@app.callback(
    [Output(component_id='prediction-content', component_property='children'),
     Output(component_id='sumo1_age', component_property='children'),
     Output(component_id='sumo1_weight', component_property='children'),
     Output(component_id='sumo1_height', component_property='children'),
     Output(component_id='sumo2_age', component_property='children'),
     Output(component_id='sumo2_weight', component_property='children'),
     Output(component_id='sumo2_height', component_property='children')],
    [Input(component_id='rikishi1_weight', component_property='value'),
     Input(component_id='rikishi1_shusshin', component_property='value'),
     Input(component_id='rikishi1_height', component_property='value'),
     Input(component_id='rikishi1_weight', component_property='value'),
     Input(component_id='rikishi2_heya', component_property='value'),
     Input(component_id='rikishi2_shusshin', component_property='value'),
     Input(component_id='rikishi2_height', component_property='value'),
     Input(component_id='rikishi2_weight', component_property='value'),
     Input(component_id='rikishi1_age', component_property='value'),
     Input(component_id='rikishi2_age', component_property='value')])
def predict(rikishi1_heya,rikishi1_shusshin,rikishi1_height,rikishi1_weight,rikishi2_heya,rikishi2_shusshin,
            rikishi2_height,rikishi2_weight, rikishi1_age,rikishi2_age):
    older = True if rikishi1_age>rikishi2_age else False
    taller = True if rikishi1_height>rikishi2_height else False
    heavier = True if rikishi1_weight>rikishi2_weight else False
    df = pandas.DataFrame(

        columns = ['rikishi1_heya','rikishi1_shusshin','rikishi1_height','rikishi1_weight','rikishi2_heya',
                   'rikishi2_shusshin','rikishi2_height','rikishi2_weight','rikishi1_age','rikishi2_age','older','taller','heavier'],
        data=[[rikishi1_heya, rikishi1_shusshin, rikishi1_height, rikishi1_weight, rikishi2_heya, rikishi2_shusshin,
               rikishi2_height, rikishi2_weight, rikishi2_age, rikishi2_age, older, taller, heavier]]
    )
    y_pred = model.predict(df)[0]
    verdict = 'Verdict: You Win' if y_pred == 1 else 'Verdict: You Lose'
    return verdict, f'Your sumos age: {rikishi1_age} years',f'Your sumos weight: {rikishi1_weight} KG', f'Your sumos height: {rikishi1_height}cm', f'opponent age: {rikishi2_age} years',f'opponent weight: {rikishi2_weight}KG',f'opponent height{rikishi2_height}cm'


