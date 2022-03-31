#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append('/usr/local/lib/python3/dist-packages')


# In[2]:


import pywraps2 as s2
from pywraps2 import S2Point, S2Cell, S2LatLng, S2LatLngRect, S1Angle, S2Loop, S2RegionCoverer, S2Polygon, S2CellId


# In[3]:


geojson = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              76.201171875,
              29.869228848968312
            ],
            [
              75.69580078125,
              28.468691297348148
            ],
            [
              77.574462890625,
              28.323724553546015
            ],
            [
              77.7392578125,
              29.35345166863502
            ],
            [
              76.201171875,
              29.869228848968312
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              71.575927734375,
              27.430289738862594
            ],
            [
              72.9052734375,
              28.159189634046708
            ],
            [
              73.17993164062499,
              27.381523191705053
            ],
            [
              71.630859375,
              27.401032392938866
            ],
            [
              72.410888671875,
              26.500072915744372
            ],
            [
              74.058837890625,
              27.36201054924028
            ],
            [
              73.5205078125,
              28.98892237190413
            ],
            [
              71.575927734375,
              27.430289738862594
            ]
          ]
        ]
      }
    }
  ]
}


# In[4]:


geojson2 = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "stroke": "#555555",
        "stroke-width": 2,
        "stroke-opacity": 1,
        "fill": "#555555",
        "fill-opacity": 0.5
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              77.0496940612793,
              28.45963668793731
            ],
            [
              77.0635986328125,
              28.45043037318006
            ],
            [
              77.05879211425781,
              28.44469488663175
            ],
            [
              77.06789016723633,
              28.436392973656965
            ],
            [
              77.07647323608398,
              28.446506126513928
            ],
            [
              77.08677291870117,
              28.449826652402077
            ],
            [
              77.09672927856445,
              28.450279443308684
            ],
            [
              77.09587097167969,
              28.462956801462703
            ],
            [
              77.07355499267578,
              28.45873118433063
            ],
            [
              77.05767631530762,
              28.467861323783215
            ],
            [
              77.0496940612793,
              28.45963668793731
            ]
          ]
        ]
      }
    }
  ]
}


# In[90]:


geo_jsons = {"km2_250":{"features":[{"properties":{},"type":"Feature","geometry":{"coordinates":[[[76.99871063232422,28.544719370308737],[76.90223693847656,28.453901700762646],[77.03922271728514,28.360286940947283],[77.15938568115234,28.472614720490967],[76.99871063232422,28.544719370308737]]],"type":"Polygon"}}],"type":"FeatureCollection"},"km2_100":{"features":[{"properties":{},"type":"Feature","geometry":{"coordinates":[[[77.02377319335936,28.559496241467098],[77.02377319335936,28.561607053766586],[76.95785522460938,28.478348692223165],[77.02720642089844,28.437902460838288],[77.10514068603516,28.51847777650959],[77.02377319335936,28.559496241467098]]],"type":"Polygon"}}],"type":"FeatureCollection"},"km2_26":{"features":[{"properties":{"stroke-width":2,"fill-opacity":0.5,"fill":"#555555","stroke-opacity":1,"stroke":"#555555"},"type":"Feature","geometry":{"coordinates":[[[77.07115173339844,28.47804691199713],[77.05741882324219,28.467936776194872],[77.05707550048828,28.4433364363651],[77.07475662231444,28.43050576788437],[77.10514068603516,28.431713426539677],[77.12196350097656,28.449222928177342],[77.10891723632812,28.46733315539307],[77.09243774414062,28.481064675455944],[77.07115173339844,28.47804691199713]]],"type":"Polygon"}}],"type":"FeatureCollection"},"km2_600":{"features":[{"properties":{},"type":"Feature","geometry":{"coordinates":[[[76.96609497070312,28.60743139267596],[76.86172485351562,28.50369515241441],[76.93588256835938,28.38415145897281],[77.08145141601562,28.370860490997323],[77.18719482421874,28.438506249680675],[77.16659545898438,28.582109884356534],[76.96609497070312,28.60743139267596]]],"type":"Polygon"}}],"type":"FeatureCollection"},"km2_50":{"features":[{"properties":{},"type":"Feature","geometry":{"coordinates":[[[77.06119537353516,28.49600133462104],[77.02875137329102,28.46914400745396],[77.0694351196289,28.42341049498704],[77.1324348449707,28.44394019419311],[77.1188735961914,28.49011744843003],[77.06119537353516,28.49600133462104]]],"type":"Polygon"}}],"type":"FeatureCollection"},"km2_960":{"features":[{"properties":{},"type":"Feature","geometry":{"coordinates":[[[76.981201171875,28.627925287618567],[76.8548583984375,28.521796040000677],[76.96746826171875,28.36361017019959],[77.17483520507812,28.34789944257093],[77.2943115234375,28.472312923883393],[77.18307495117188,28.63395214251842],[76.981201171875,28.627925287618567]]],"type":"Polygon"}}],"type":"FeatureCollection"}}


# In[5]:


from typing import Dict

class GeoJsonParser:
    
    def __init__(self, geojson: Dict):
        self.geojson = geojson
        self.polygons = []
        self.loops = []
        
        ## parse the GeoJson
        self.parse_geojson()
        self.get_loops()
        
    def parse_geojson(self):
        features = self.geojson['features']
        for feature in features:
            latlngs = []
            coordinates = feature['geometry']['coordinates']
            for coordinate in coordinates[0][:-1]:
                latlngs.append(S2LatLng.FromDegrees(coordinate[1], coordinate[0]))
            self.polygons.append(latlngs)
            
    def get_loops(self):
        for poly in self.polygons:
            s2loop = []
            for latlng in poly:
                s2loop.append(latlng.ToPoint())
            self.loops.append(s2loop)


def get_region_cover(min_level: int, max_level: int, geojson: Dict):
  parser = GeoJsonParser(geojson)
  loop = S2Loop(parser.loops[0])
  poly = S2Polygon(loop)
  coverer = S2RegionCoverer()
  coverer.set_min_level(min_level)
  coverer.set_max_level(max_level)
  cells = coverer.GetCovering(poly)