from dash import html

# pylint: disable=import-error
import dash_bootstrap_components as dbc
import src.components.map as map_component
import src.components.controls as controls_component  # type: ignore


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
            dbc.Modal(
                [
                    dbc.ModalHeader(
                        dbc.ModalTitle(
                            "Hello World!",
                            style={"fontSize": "xx-large"},
                        ),
                        id="modal-header",
                        close_button=True,
                    ),
                    dbc.ModalBody(
                        html.Div(
                            [
                                html.Img(
                                    src="assets/diagram.svg",
                                    style={
                                        "width": "100%",
                                    },
                                ),
                            ],
                        ),
                        style={
                            "alignSelf": "center",
                            "width": "90%",
                        },
                    ),
                ],
                id="modal",
                is_open=False,
                size="xl",
            ),
            dbc.Spinner(
                children=html.Div(id="loading-output"),
                fullscreen=True,
                fullscreen_style={
                    "backgroundColor": "rgba(255, 255, 255, 0.1)",
                },
                # show_initially=False,
            ),
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
