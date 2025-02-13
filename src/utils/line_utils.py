from matplotlib.colors import LinearSegmentedColormap


def calculate_direction_diff(heading: int, bearing: int, forgrening: str):
    """
    Calculate the difference between
    heading_calc and bearing.

    Returns:
        float: The difference in heading and bearing.
    """
    rev_bearing = (bearing + 180) % 360

    # One way streets listed in wrong direction
    reverse = ["2", "2A", "4", "6", "6A", "8"]

    # One way streets
    one_way = ["1", "1A", "3", "3A", "5", "5A", "7", "7A"]

    heading_diff = min(abs(heading - bearing), 360 - abs(heading - bearing))
    rev_heading_diff = min(
        abs(heading - rev_bearing),
        360 - abs(heading - rev_bearing),
    )

    if any(rev == forgrening for rev in reverse):
        result = rev_heading_diff

    elif any(ow == forgrening for ow in one_way):
        result = heading_diff

    else:
        result = min(heading_diff, rev_heading_diff)

    return result


def rgba_to_rgb(rgba):
    """Convert RGBA tuple to 'rgb(r, g, b)' string."""
    r, g, b, _ = [int(c * 255) for c in rgba]  # Convert to 0-255 range
    return f"rgb({r}, {g}, {b})"  # Format as CSS-compatible RGB


def get_color_from_angle(angle):
    """
    Get the RGBA color corresponding to an angle (0-360°).
    """
    colors = [
        (0, 0.404, 0.106, 1),  # Color 1
        (0.004, 0.518, 0.286, 1),  # Color 2
        (0.008, 0.471, 0.525, 1),  # Color 3
        (0.012, 0.412, 0.773, 1),  # Color 4
        (0, 0.322, 1, 1),  # Color 5
        (0.012, 0.412, 0.773, 1),  # Color 6 (same as Color 4)
        (0.008, 0.471, 0.525, 1),  # Color 7 (same as Color 3)
        (0.004, 0.518, 0.286, 1),  # Color 8 (same as Color 2)
        (0, 0.404, 0.106, 1),  # Color 9 (same as Color 1)
    ]
    # Create custom colormap
    cmap = LinearSegmentedColormap.from_list("conic_gradient", colors, N=360)
    color = cmap(angle)

    return rgba_to_rgb(color)
