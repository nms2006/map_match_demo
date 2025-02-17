# flake8: noqa
# pylint: disable=unused-import

from dash import Dash
import dash_bootstrap_components as dbc  # pylint: disable=import-error
from src.components import layout


from src.callbacks import (
    control_callbacks,
    map_callbacks,
    style_callbacks,
)

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.DARKLY,
        dbc.icons.BOOTSTRAP,
    ],
)
server = app.server
app.layout = layout.create_layout()  # Set the layout

if __name__ == "__main__":
    app.run_server(debug=False)
