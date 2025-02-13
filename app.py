from dash import Dash  # type: ignore[import-untyped]
from src.components import layout

from src.callbacks import (
    control_callbacks,
    map_callbacks,
    style_callbacks,
)

app = Dash(
    __name__,
    external_stylesheets=["/assets/style.css"],
)
app.layout = layout.create_layout()  # Set the layout

if __name__ == "__main__":
    app.run_server(debug=True, port=8060)
