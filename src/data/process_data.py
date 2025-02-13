def group_data_by_sampletime(data: dict):
    lines_by_sampletime = {}
    for feature in data["features"]:
        sampletime = feature["properties"]["SAMPLE_TIME"]
        point = feature["geometry"]["coordinates"]
        point = [point[1], point[0]]  # Swap lat, long
        line_geometry = feature["properties"].get("line_geometry", [])
        heading = feature["properties"].get("heading_calc", None)
        bearing = feature["properties"].get("bearing", [])
        forgrening = feature["properties"].get("FORGRENING", [])

        if sampletime not in lines_by_sampletime:
            lines_by_sampletime[sampletime] = {
                "point": point,
                "lines": [],
                "heading": heading,
                "bearing": [],
                "forgrening": [],
            }

        if line_geometry:
            lines_by_sampletime[sampletime]["lines"].append(line_geometry)
        if bearing:
            lines_by_sampletime[sampletime]["bearing"].append(bearing)
        if forgrening:
            lines_by_sampletime[sampletime]["forgrening"].append(forgrening)

    return lines_by_sampletime
