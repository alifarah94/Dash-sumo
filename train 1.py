import dash
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)





import pandas as pd
from category_encoders import *
from sklearn.linear_model import LogisticRegression


sumo_matches = pd.read_csv('https://query.data.world/s/kp5eazhvwdbrnhhyow5lm4kfywhyvg') # fight result dataframe
sumo_info = pd.read_csv('https://query.data.world/s/6gckbhyl6klbem3vs25chgcaw65gfa') # sumo info dataframe

sumo_info = sumo_info.dropna()
sumo_info_2 = sumo_info.drop(['rank','rikishi','prev','prev_w','prev_l'],axis=1)

sumo_1 = sumo_info_2.copy()
sumo_2 = sumo_info_2.copy()


sumo_1 = sumo_1.rename(columns={"id":"rikishi1_id","weight": "rikishi1_weight","height":"rikishi1_height","heya": "rikishi1_heya","shusshin":"rikishi1_shusshin","birth_date": "rikishi1_birthday"})
sumo_2 = sumo_2.rename(columns={"id":"rikishi2_id","weight": "rikishi2_weight","height":"rikishi2_height","heya": "rikishi2_heya","shusshin":"rikishi2_shusshin","birth_date": "rikishi2_birthday"})

sumo_matches_1 = sumo_matches.loc[(sumo_matches.index%2)==0]

sumo_matches_rik1 = pd.merge(sumo_matches_1,sumo_1,how='left',on=['basho','rikishi1_id'])
sumo_matches_rik1_rik2 = pd.merge(sumo_matches_rik1,sumo_2,how='left',on=['basho','rikishi2_id'])

df = sumo_matches_rik1_rik2
df = df.dropna()

target = 'rikishi1_win'
features = df.drop(columns=['rikishi1_win','rikishi2_win'])
features = features.columns

train, test = train_test_split(df, train_size=0.80, test_size=0.20, 
                              stratify=df['rikishi1_win'], random_state=42)

x_train = train[features]
y_train = train[target]

pipeline = make_pipeline(
    ce.OrdinalEncoder(),
    StandardScaler(),
    LogisticRegression()
)

pipeline.fit(x_train,y_train)











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












if __name__ == '__main__':
    app.run_server(debug=True)