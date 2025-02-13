import dash_bootstrap_components as dbc
from dash import html


def create_popup():
    return (
        dbc.Modal(
            [
                dbc.ModalHeader(
                    dbc.ModalTitle(
                        "Diagram til overgang mellem veje.",
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
    )


def full_screen_spinner():
    return dbc.Spinner(
        children=html.Div(id="loading-output"),
        color="primary",
        fullscreen=True,
        fullscreen_style={
            "backgroundColor": "rgba(255, 255, 255, 0.1)",
        },
    )
