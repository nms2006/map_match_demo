import re


def parse_line_string(line_string):
    coords = re.findall(r"([-\d\.]+) ([\d\.]+)", line_string)
    return [[float(coord[1]), float(coord[0])] for coord in coords]


def fix_line_coordinates(line):
    if isinstance(line, str):
        return parse_line_string(line)
    elif isinstance(line, list):
        return [[coord[1], coord[0]] for coord in line]  # Swap lat, long
    return []
