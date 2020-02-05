import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html



app = dash.Dash()
app.title = 'Sumo'
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})


#app.layout = 
    #html.H1(children='Sumo'),
    
    #html.Div(children='''
    
  #      Dash: A web application framework for Python.
   # ''')

app.layout = html.Div([
        html.Div([
            html.Div([
                html.H1(children='Sumo')
                ],className='six.columns'),
            html.Div([
                 html.H2(children='Sumo1'),
            ],className='six.columns')
            
        
        ],className= "row"),
    ])





if __name__ == '__main__':
    app.run_server(debug=True)