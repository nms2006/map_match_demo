from dash import html

# pylint: disable=import-error
import src.components.map as map_component
import src.components.controls as controls_component
import src.components.popup as popup_component


def create_layout():
    return html.Div(
        style={
            "backgroundColor": "#2E2E2E",
            "backgroundSize": "auto",
            "color": "#FFFFFF",
            "border": "none",
            "height": "100vh",
            "width": "100vw",
            "outlineOffset": "0px",
            "margin": "0px 0px 0px 0px",
            "padding": "0px 0px 0px 0px",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "fontFamily": "Arial, sans-serif",
        },
        children=[
            popup_component.create_popup(),
            popup_component.full_screen_spinner(),
            html.Div(
                style={
                    "display": "flex",
                    "flexDirection": "row",
                    "gap": "1vw",
                    "alignItems": "center",
                },
                children=[
                    map_component.create_map(),
                    controls_component.create_controls(),
                ],
            ),
        ],
    )
