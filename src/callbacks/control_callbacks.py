from dash import (
    callback,
    Output,
    Input,
)


@callback(
    Output("interval", "disabled"),
    Input("play-pause-button", "children"),
)
def interval_state(radio_value: str):
    if radio_value == "Play":
        return True
    else:
        return False


@callback(
    Output("play-pause-button", "children"),
    Input("play-pause-button", "n_clicks"),
)
def toggle_play_pause(n_clicks):
    return "Pause" if n_clicks % 2 else "Play"


@callback(
    Output("modal", "is_open"),
    Input("probabilities", "value"),
    prevent_initial_call=True,
)
def toggle_modal(selected_value):

    if selected_value == "transition":
        return True
    else:
        return False
