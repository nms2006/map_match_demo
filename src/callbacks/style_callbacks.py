from dash import callback, Output, Input, State  # type: ignore[import-untyped]
from src.callbacks.map_callbacks import processed_forward


@callback(
    Output("next-button", "style"),
    Output("back-button", "style"),
    Output("prob-container", "style"),
    Input("play-pause-button", "children"),
    Input("points", "children"),
    State("next-button", "style"),
    State("back-button", "style"),
    State("prob-container", "style"),
    State("click-store", "data"),
)
def toggle_buttons(
    control_value,
    points,
    next_button_style,
    back_button_style,
    prob_style,
    all_clicks,
):
    all_childs = len(points)

    if control_value == "Pause":
        # Hide both buttons when playing
        next_button_style["display"] = "none"
        back_button_style["display"] = "none"
        prob_style["display"] = "none"
    elif control_value == "Play" and all_childs == 0:
        # Hide only the "Previous Timestamp" button if there are no markers
        back_button_style["display"] = "none"
        next_button_style["display"] = "flex"  # Ensure next button is visible
        prob_style["display"] = "none"
    else:
        # Ensure both buttons are visible when paused and markers exist
        next_button_style["display"] = "flex"
        back_button_style["display"] = "flex"
        prob_style["display"] = "block"

    if all_clicks >= len(processed_forward):
        prob_style["display"] = "none"

    return next_button_style, back_button_style, prob_style


@callback(
    Output("gradient", "style"),
    Input("probabilities", "value"),
    State("gradient", "style"),
)
def toggle_gradient(prob_value, gradient_style):
    if prob_value != "emission":
        gradient_style["display"] = "none"
    else:
        gradient_style["display"] = "block"

    return gradient_style


@callback(
    Output("finish-button", "style"),
    Input("finish-button", "n_clicks"),
    State("finish-button", "style"),
)
def remove_finish_button(n_clicks, style):
    if n_clicks == 1:
        style["display"] = "none"
        return style
    else:
        return style
