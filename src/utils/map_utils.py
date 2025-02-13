import math
import dash_leaflet as dl  # type: ignore[import-untyped]
from src.data.process_lines import fix_line_coordinates


def process_lines_with_fix(lines, color, children):
    """Fixes line coordinates and returns Polyline objects."""
    return [
        dl.Polyline(
            positions=fix_line_coordinates(line),
            pathOptions={"color": color},
            children=children,
        )
        for line in lines
        if fix_line_coordinates(line)
    ]


def create_point_marker(point, color, children):
    """Creates a Circle marker for a given point."""
    return dl.Circle(
        center=point,
        radius=5,
        pathOptions={"color": color},
        children=children,
    )


def create_heading_line(point, heading, color, children):
    """Creates a heading direction line for a given point and heading."""
    if heading is None:
        return None
    heading_length = 0.0006  # Adjust for visualization
    heading_rad = math.radians(heading)
    end_point = [
        point[0] + heading_length * math.cos(heading_rad),
        point[1] + heading_length * math.sin(heading_rad),
    ]
    return dl.Polyline(
        positions=[point, end_point],
        pathOptions={"color": color},
        id="heading",
        children=children,
    )
