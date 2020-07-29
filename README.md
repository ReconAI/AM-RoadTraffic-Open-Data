# AM-RoadTraffic-Open-Data

Collect available cameras and image links from https://www.digitraffic.fi/en/road-traffic/

Separate sheet contains the [relevant data fields](https://docs.google.com/spreadsheets/d/1WUtCOKE_0hewp8PUAj17-Y_PuWtn4BlfjuH1g4nDqNI/edit#gid=0) which are available.

## Usage:

- Install requests library
- Use python2.7 (can be modified to python3 as well)
- python2 collect_available_image_data.py

## Returns:

First line is:
- roadStationId;latitude;longitude;collectionInterval;name;roadNumber;roadSection;distanceFromRoadSectionStart;presentationName;resolution;direction;imageUrl

Second line and lines after that are the values similar to this:
- 1502;25.616391;60.390238;720;Road 7 Porvoo, Harabacka;7;8;3801;Porvoo;704x576;UNKNOWN;http://weathercam.digitraffic.fi/C0150200.jpg
