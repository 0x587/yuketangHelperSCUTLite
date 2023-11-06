from dash import Dash, html, callback, Input, Output, ALL
import dash_mantine_components as dmc

params = {
    'csrf_token': "",  # 需改成自己的
    'session_id': "",  # 需改成自己的
    'university_id': "",  # 需改成自己的
    'url_root': "https://*****.yuketang.cn/",  # 按需修改域名 example:https://*****.yuketang.cn/
}

app = Dash(__name__)

app.layout = dmc.Container([
    dmc.Text(id='title'),
    *[
        dmc.TextInput(id={'type': 'params-input', 'key': k}, label=k, value=v, required=True)
        for k, v in params.items()
    ],
    dmc.Button('Login', id='login'),
    dmc.Text('User ID: ', id='user-id'),
    dmc.Text('Classroom ID: ', id='classroom-id'),
    dmc.CheckboxGroup(
        id='course-check',
        description='chose your course',
        orientation='vertical',
        offset="md",
        mb=16,
        children=[
            dmc.Checkbox(label="React", value="react"),
            dmc.Checkbox(label="Vue", value="vue"),
            dmc.Checkbox(label="Svelte", value="svelte"),
            dmc.Checkbox(label="Angular", value="angular"),
        ]
    ),
    dmc.Button('Start', id='start'),
])


@callback(
    Output('title', component_property='children'),
    Input({'type': 'params-input', 'key': ALL}, 'value'),
)
def call(v):
    csrf_token, session_id, university_id, url_root = v
    params['csrf_token'] = csrf_token
    params['session_id'] = session_id
    params['university_id'] = university_id
    params['url_root'] = url_root
    return None


@callback(
    Output('user-id', 'children'),
    Output('classroom-id', 'children'),
    Input('login', 'n_clicks'),
    prevent_initial_call=True,
)
def login(n_clicks):
    return 'User ID: 123', 'Classroom ID: 567'


if __name__ == '__main__':
    app.run(debug=True)
