from dash import Dash, html, dcc, callback, Input, Output, dash_table
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd 
import plotly.express as px 

df = pd.read_csv("data/df.csv")
df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(external_stylesheets=external_stylesheets)

app.layout = dbc.Row(
    dmc.Container(
        html.Div([    
            html.H1(children='Title of the App', style ={'textAlign':'center'}),
            html.Hr(),
            dcc.Dropdown(options=df['country'].unique(), value='Canada', id = 'dropdown_selection'),
            dcc.Graph(id = 'graph_content'),
            dcc.RadioItems(options = ['pop', 'lifeExp', 'gdpPercap'], value = 'lifeExp', id='controls-and-radio-item', inline=True),
            dcc.Graph(id = 'graph_second', figure=px.histogram(data_frame = df2, x='continent', y='lifeExp', histfunc='avg')),
            dash_table.DataTable(data = df2.to_dict('records'), page_size=10)        
        ]))
)

@callback(
    Output(component_id = 'graph_content', component_property='figure'),
    Input(component_id = 'dropdown_selection', component_property='value')
)
def update_graph(value):
    dff = df[df['country'] == value]
    return px.line(data_frame=dff, x='year', y='pop')

@callback(
    Output('graph_second', 'figure'),
    Input('controls-and-radio-item', 'value')
)
def update_graph2(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

if __name__ == "__main__":
    app.run(debug=True)