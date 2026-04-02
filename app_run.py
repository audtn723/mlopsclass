from dash import Dash
from dash.dependencies import Input, Output, State
import plotly.express as px
import app_layout as al
import mylib as my

DB_NAME = "postgres"
DB_HOST = "172.17.0.2"

df = my.db_to_df(DB_HOST=DB_HOST, DB_NAME=DB_NAME, table_name="predict")

items = ['button1', 'dropdown1', 'graph1', df]

app = Dash()
app.layout = al.app_layout(items)

@app.callback(
    Output('graph1', 'figure'),
    Input('button1', 'n_clicks'),
    State('dropdown1', 'value'),
    prevent_initial_call=False,
)
def fn(n_clicks, value):
    df = my.db_to_df(DB_HOST=DB_HOST, DB_NAME=DB_NAME, table_name="predict")
    fig = px.histogram(df, x=value, width=700, height=400)
    return fig

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8050)
