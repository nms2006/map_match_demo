import math
from dash import (
    callback,
    Output,
    Input,
    State,
    no_update,
)
import dash_leaflet as dl
import json
from src.data.process_data import group_data_by_sampletime
from src.data.process_lines import fix_line_coordinates
from src.components.map import get_initial_center
from src.utils.line_utils import (
    calculate_direction_diff,
    get_color_from_angle,
)
from src.utils.map_utils import (
    create_heading_line,
    create_point_marker,
    process_lines_with_fix,
)

# Load GeoJSON files once
with open("src/data/forward.geojson", "r") as f:
    forward = json.load(f)
    processed_forward = group_data_by_sampletime(forward)

with open("src/data/backward.geojson", "r") as f:
    backward = json.load(f)
    processed_backward = group_data_by_sampletime(backward)


@callback(
    Output("points", "children", allow_duplicate=True),
    Output("lines", "children", allow_duplicate=True),
    Output("map", "center", allow_duplicate=True),
    Output("click-store", "data", allow_duplicate=True),
    Input("interval", "n_intervals"),
    Input("next-button", "n_clicks"),
    State("points", "children"),
    State("lines", "children"),
    State("map", "center"),
    State("click-store", "data"),
    prevent_initial_call=True,
)
def animate_lines(
    _,
    __,
    points,
    lines,
    map_center,
    all_clicks,
):
    sampletimes = sorted(processed_forward.keys())
    n_intervals = all_clicks

    if n_intervals < len(sampletimes):

        sampletime = sampletimes[n_intervals]
        sample_data = processed_forward[sampletime]

        point = sample_data["point"]
        heading = sample_data["heading"]
        map_center = point
        line_coordinates = sample_data["lines"]

        points.append(create_point_marker(point, "red", n_intervals))
        lines.extend(
            process_lines_with_fix(
                line_coordinates,
                "blue",
                n_intervals,
            )
        )

        heading_line = create_heading_line(point, heading, "red", n_intervals)
        if heading_line:
            lines.append(heading_line)

    elif n_intervals - len(sampletimes) >= 0:
        backward_idx = len(sampletimes) - (n_intervals - len(sampletimes)) - 1
        backward = sorted(processed_backward.keys())
        backtime = backward[backward_idx]
        sample_data = processed_backward[backtime]

        for d in lines:
            if (
                d["props"].get("children") == backward_idx
                and d["props"]["pathOptions"].get("color") == "red"
            ):
                d["props"]["pathOptions"].update({"color": "green"})
            elif (
                d["props"].get("children") >= backward_idx
                and d["props"]["pathOptions"].get("color") == "blue"
            ):
                d["props"]["pathOptions"].update({"opacity": "0"})

        for d in points:
            if d["props"].get("children") == backward_idx:
                d["props"]["pathOptions"].update(
                    {
                        "color": "green",
                    }
                )
        point = sample_data["point"]
        map_center = point
        line_coordinates = sample_data["lines"]

        lines.extend(
            process_lines_with_fix(
                line_coordinates,
                "blue",
                n_intervals,
            )
        )

    return (
        points,
        lines,
        map_center,
        all_clicks + 1,
    )


@callback(
    Output("points", "children", allow_duplicate=True),
    Output("lines", "children", allow_duplicate=True),
    Output("map", "center", allow_duplicate=True),
    Output("click-store", "data", allow_duplicate=True),
    Input("back-button", "n_clicks"),
    State("points", "children"),
    State("lines", "children"),
    State("map", "center"),
    State("click-store", "data"),
    prevent_initial_call=True,
)
def backtrack(
    _,
    points,
    lines,
    map_center,
    all_clicks,
):
    step = all_clicks - 1
    sampletimes = sorted(processed_forward.keys())

    if step > 0 and all_clicks < len(sampletimes):
        points = [d for d in points if d["props"].get("children") < step]
        lines = [d for d in lines if d["props"].get("children") < step]
        map_center = next(
            (
                d["props"]["center"]
                for d in points
                if d["props"].get("children") == step - 1
            ),
            None,
        )
    elif step > 0 and all_clicks - len(sampletimes) >= 0:
        idx = 2 * len(sampletimes) - step - 1

        for d in lines:
            if (
                d["props"].get("children") == idx
                and d["props"].get("id") == "heading"  # noqa: E501
            ):
                d["props"]["pathOptions"].update({"color": "red"})

        lines = [
            d
            for d in lines
            if not (
                d["props"].get("children") == idx
                and d["props"]["pathOptions"].get("color") == "green"
            )
        ]

        for d in lines:
            if (
                d["props"].get("children") == idx
                and d["props"]["pathOptions"].get("color") == "blue"
            ):
                d["props"]["pathOptions"].update({"opacity": "1"})

        for d in points:
            if d["props"].get("children") == idx:
                d["props"]["pathOptions"].update(
                    {
                        "color": "red",
                    }
                )

        map_center = next(
            (
                d["props"]["center"]
                for d in points
                if d["props"].get("children") == idx + 1
            ),
            None,
        )

    else:
        points = []
        lines = []
        map_center = get_initial_center()

    return points, lines, map_center, all_clicks - 1


@callback(
    Output("emission", "children"),
    Output("lines", "children", allow_duplicate=True),
    Input("probabilities", "value"),
    Input("click-store", "data"),
    Input("lines", "children"),
    prevent_initial_call=True,
)
def highlight_emission(prob_value, all_clicks, normal_lines):
    current_stage = all_clicks - 1
    sampletimes = sorted(processed_forward.keys())
    if all_clicks < len(sampletimes):
        if prob_value == "emission":
            lines = []

            for d in normal_lines:
                if (
                    d["props"].get("children") <= current_stage
                    and d["props"]["pathOptions"].get("color") == "blue"
                ):
                    d["props"]["pathOptions"].update({"opacity": "0"})

            sampletimes = sorted(processed_forward.keys())
            sampletime = sampletimes[current_stage]
            sample_data = processed_forward[sampletime]

            heading = sample_data["heading"]
            line_coordinates = sample_data["lines"]
            bearings = sample_data["bearing"]
            forgreninger = sample_data["forgrening"]

            for line, bearing, forgrening in zip(
                line_coordinates,
                bearings,
                forgreninger,
            ):
                diff = calculate_direction_diff(heading, bearing, forgrening)
                line_color = get_color_from_angle(math.floor(diff))

                if fix_line_coordinates(line):
                    lines.append(
                        dl.Polyline(
                            positions=fix_line_coordinates(line),
                            pathOptions={"color": f"{line_color}"},
                            weight=5,
                        )
                    )

            return lines, normal_lines
        else:
            for d in normal_lines:
                if (
                    d["props"].get("children") <= current_stage
                    and d["props"]["pathOptions"].get("color") == "blue"
                ):
                    d["props"]["pathOptions"].update(
                        {
                            "opacity": "1",
                        }
                    )

            return [], normal_lines
    else:
        return [], normal_lines


@callback(
    Output("points", "children", allow_duplicate=True),
    Output("lines", "children", allow_duplicate=True),
    Output("map", "center", allow_duplicate=True),
    Output("click-store", "data", allow_duplicate=True),
    Output("loading-output", "children", allow_duplicate=True),
    Input("finish-button", "n_clicks"),
    State("points", "children"),
    State("lines", "children"),
    State("map", "center"),
    State("click-store", "data"),
    prevent_initial_call=True,
)
def finish_algorithm(_, points, lines, map_center, all_clicks):
    sampletimes = sorted(processed_forward.keys())
    full = len(sampletimes)

    for idx in range(all_clicks, full):
        sampletime = sampletimes[idx]
        sample_data = processed_forward[sampletime]

        point = sample_data["point"]
        heading = sample_data["heading"]
        map_center = point
        line_coordinates = sample_data["lines"]

        points.append(create_point_marker(point, "red", idx))
        lines.extend(process_lines_with_fix(line_coordinates, "blue", idx))

        heading_line = create_heading_line(point, heading, "red", idx)
        if heading_line:
            lines.append(heading_line)

    return (
        points,
        lines,
        map_center,
        full,
        no_update,
    )
