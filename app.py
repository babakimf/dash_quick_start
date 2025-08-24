from dash import Dash, html, dcc, callback, Input, Output
import pandas as pd 
import plotly.express as px 

df = pd.read_csv("data/df.csv")

app = Dash()

app.layout = [
    html.H1(children='Title of the App', style ={'textAlign':'center'}),
    dcc.Dropdown(options=df['country'].unique(), value='Canada', id = 'dropdown_selection'),
    dcc.Graph(id = 'graph_content')
]

@app.callback(
    Output(component_id = 'graph_content', component_property='figure'),
    Input(component_id = 'dropdown_selection', component_property='value')
)
def update_graph(value):
    dff = df[df['country'] == value]
    return px.line(data_frame=dff, x='year', y='pop')

if __name__ == "__main__":
    app.run(debug=True)