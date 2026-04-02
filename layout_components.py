from dash import html, dash_table, dcc

def showtable(idname, dataframe, max_rows=100):
    return dash_table.DataTable(
        id=idname,
        columns=[{"name": i, "id": i} for i in dataframe.columns],
        data=dataframe[:max_rows].to_dict('records'),
        page_action='none',
        fixed_rows={'headers': True},
        style_table={'height': '300px', 'overflowY': 'auto'}
    )

def showgraph(idname):
    return dcc.Graph(id=idname)

def button(idname, text):
    return html.Button(text, id=idname, n_clicks=0)

def dropdown_menu(idname, menu):
    return dcc.Dropdown(
        id=idname,
        options=[{"label": name, "value": name} for name in menu],
        value=menu[0],
        placeholder='select value'
    )
