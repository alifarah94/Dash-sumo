import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html



app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css'])
app.title = 'Sumo'






app.layout = html.Div
( 
html.Div(
    [                                       
        html.Div(
            [                                                  
                html.H1(children=' ',
                className='six columns'),
                html.Div(children='Sumo Project')
            ],className="row"),
        html.Div(
            [   
                html.Div(children=' ',
                className='three columns'),
                html.Div(children='sumo',
                className='nine columns')

            ],className="row")

    ]
        )
)

if __name__ == '__main__':
    app.run_server(debug=False)


