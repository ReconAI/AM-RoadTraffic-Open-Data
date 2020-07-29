# -*- coding: utf-8 -*-
"""
Read JSON data of images
https://www.digitraffic.fi/en/road-traffic/
"""
import requests

def build_list_of_cameras_online():
    # Read online cameras from the JSON data
    json_data = get_all_camera_data()
    road_stations = json_data.get("features", [])
    print("roadStationId;latitude;longitude;collectionInterval;name;roadNumber;roadSection;distanceFromRoadSectionStart;presentationName;resolution;direction;imageUrl")
    # 16593,23.333591,60.376029,720,Road 1 Salo, Hepomäki beam west,1,21,6734,Hepomäki,704x576,UNKNOWN,http://weathercam.digitraffic.fi/C1659300.jpg
    for station in road_stations:
        lines = []
        lines.append(str(station.get("id", "")))
        coordinates = station.get("geometry", {}).get("coordinates", ["None", "None"])
        lines.append(str(coordinates[0]))
        lines.append(str(coordinates[1]))
        properties = station.get("properties", {})
        lines.append(str(properties.get("collectionInterval", "")))
        lines.append(properties.get("names", {}).get("en", ""))
        roadAddress = properties.get("roadAddress", {})
        lines.append(str(roadAddress.get("roadNumber", "")))
        lines.append(str(roadAddress.get("roadSection", "")))
        lines.append(str(roadAddress.get("distanceFromRoadSectionStart", "")))
        presets = properties.get("presets", [])
        for direction in presets:
            if direction.get("inCollection"):
                presentationName = direction.get("presentationName", "")
                if presentationName:
                    lines.append(presentationName)
                lines.append(str(direction.get("resolution", "")))
                lines.append(str(direction.get("direction", "")))
                lines.append(str(direction.get("imageUrl", "")))
        print(";".join(lines))

def get_all_camera_data():
    # Get all cameras as JSON data
    url = "https://tie.digitraffic.fi/api/v3/metadata/camera-stations"
    response = requests.get(url=url)
    if response.status_code != 200:
        return False
    json_data = response.json()
    return json_data

def main():
    # Read JSON data of images
    # https://www.digitraffic.fi/en/road-traffic/
    build_list_of_cameras_online()

if __name__ == '__main__':
    main()
