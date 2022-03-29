#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
sys.path.append('/usr/local/lib/python3/dist-packages')


# In[3]:


from pywraps2 import S2Point, S2Cell, S2LatLng, S2LatLngRect, S1Angle, S2Loop, S2RegionCoverer


# In[4]:


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


# In[5]:


class GeoJsonParser:
    
    def __init__(self, geojson: dict):
        self.geojson = geojson
        self.polygons = []
        self.loops = []
        
        ## parse the GeoJson
        self.parse_geojson()
        self.get_loops()
        
    def parse_geojson(self):
        features = geojson['features']
        for feature in features:
            latlngs = []
            coordinates = feature['geometry']['coordinates']
            for coordinate in coordinates[0]:
                latlngs.append(S2LatLng.FromDegrees(coordinate[1], coordinate[0]))
            self.polygons.append(latlngs)
            
    def get_loops(self):
        for poly in self.polygons:
            s2loop = []
            for latlng in poly:
                s2loop.append(latlng.ToPoint())
            self.loops.append(s2loop)


# In[7]:


parser = GeoJsonParser(geojson)
for point in parser.loops[0]:
    print(point)
    
parser.loops[0].pop(3)
parser.loops[0]


# In[ ]:


print(S2Loop(parser.loops[0]))


# In[ ]:




