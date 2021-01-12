#%%
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from dwcl import DashWindowCloseListener
from flask import request
from plotly import graph_objects as go

app = dash.Dash()
app.title = "Demo"
app.layout = html.Div(
    children=[
        DashWindowCloseListener(id="my-closed-listener"),
        html.Span(id="page-listener-dummy"),
        html.Div("your content"),
    ],
)


@app.callback(
    Output("page-listener-dummy", "children"), [Input("my-closed-listener", "status")]
)
def detect_close(status):
    print(f"Status: {status}")
    if status is None or status == "mounted":
        return None
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()


if __name__ == "__main__":
    app.run_server(debug=True)
