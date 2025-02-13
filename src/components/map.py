import dash_leaflet as dl  # type: ignore[import-untyped]
from dash import html  # type: ignore[import-untyped]
import json

# Load GeoJSON Data (Only Once)
with open("geoapp/data/forward.geojson", "r") as f:
    forward = json.load(f)


def get_initial_center():
    first_point = forward["features"][0]["geometry"]["coordinates"]
    return [first_point[1], first_point[0]]  # Swap lat, long


def create_map():
    return html.Div(
        style={
            "width": "90vw",
            "height": "90vh",
            "border": "2px solid #FFFFFF",
            "borderRadius": "10px",
            "overflow": "hidden",
        },
        children=[
            dl.Map(
                center=get_initial_center(),
                zoom=16,
                id="map",
                style={"width": "100%", "height": "100%"},
                preferCanvas=True,
                children=[
                    dl.TileLayer(
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    ),
                    dl.FeatureGroup(children=[], id="points"),
                    dl.FeatureGroup(children=[], id="emission"),
                    dl.FeatureGroup(children=[], id="lines"),
                ],
            ),
        ],
    )
