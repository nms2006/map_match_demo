from dash import dcc, html  # type: ignore[import-untyped]
from src.utils.button_utils import button_style


def create_controls():
    return html.Div(
        style={
            "display": "flex",
            "flexDirection": "column",
            "gap": "1vw",
            "width": "8vw",
            "justifyContent": "flex-start",
            "alignItems": "center",
            "minWidth": "100px",
            "marginBottom": "auto",
        },
        children=[
            # html.Div(
            #     id="gradient",
            #     style={
            #         "width": "100%",
            #         "aspectRatio": "1",
            #         "borderRadius": "50%",
            #         "background": (
            #             "conic-gradient(from 0deg, "
            #             "rgba(0,103,27,1), "
            #             "rgba(1,132,73,1), "
            #             "rgba(2,120,134,1), "
            #             "rgba(3,105,197,1), "
            #             "rgba(0,82,255,1), "
            #             "rgba(3,105,197,1), "
            #             "rgba(2,120,134,1), "
            #             "rgba(1,132,73,1), "
            #             "rgba(0,103,27,1)"
            #         ),
            #         "marginBottom": "20px",
            #     },
            # ),
            html.Div(
                id="gradient",
                style={
                    "width": "100%",  # Full width
                    "height": "20px",  # Adjust height as needed
                    "borderRadius": "5px",  # Rounded edges for a smooth look
                    "background": (
                        "linear-gradient(to left, "
                        "rgba(0,103,27,1), "
                        "rgba(1,132,73,1), "
                        "rgba(2,120,134,1), "
                        "rgba(3,105,197,1), "
                        "rgba(0,82,255,1))"
                    ),
                    "position": "relative",
                    "marginBottom": "20px",
                },
                children=[
                    # Labels at 0, 50, and 100 positions
                    html.Div(
                        "0",
                        style={
                            "position": "absolute",
                            "left": "0%",
                            "top": "25px",
                            "color": "white",
                        },
                    ),
                    html.Div(
                        "1",
                        style={
                            "position": "absolute",
                            "right": "0%",
                            "top": "25px",
                            "color": "white",
                        },
                    ),
                ],
            ),
            html.Button(
                "Play",
                id="play-pause-button",
                n_clicks=0,
                style=button_style(),
            ),
            html.Div(
                id="prob-container",
                children=[
                    dcc.RadioItems(
                        id="probabilities",
                        options=[
                            {"label": "Off", "value": "off"},
                            {"label": "Emission", "value": "emission"},
                            {"label": "Transition", "value": "transition"},
                        ],
                        value="off",
                        style={
                            "padding": "10px 20px",
                            "cursor": "pointer",
                            "fontSize": "16px",
                        },
                    ),
                ],
                style={
                    "backgroundColor": "#444444",
                    "color": "#FFFFFF",
                    "border": "none",
                    "width": "100%",
                    "borderRadius": "5%",
                    "display": "none",  # Initially hidden
                },
            ),
            dcc.Interval(
                id="interval",
                interval=600,
                n_intervals=0,
                disabled=True,
            ),
            html.Div(
                id="button-container",
                style={
                    "gap": "1vw",
                    "width": "100%",
                    "display": "flex",
                    "flex-direction": "column",
                },
                children=[
                    html.Button(
                        "Next Timestamp",
                        id="next-button",
                        style=button_style(),
                    ),
                    html.Button(
                        "Previous Timestamp",
                        id="back-button",
                        style=button_style(),
                    ),
                ],
            ),
            html.Button(
                "Finish Algorithm",
                id="finish-button",
                n_clicks=0,
                style=button_style(),
            ),
            dcc.Store(id="click-store", data=0),
        ],
    )
