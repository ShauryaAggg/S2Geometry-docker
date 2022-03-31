#!/usr/bin/env python
# coding: utf-8

# In[2]:


import h3
import pandas as pd
import time
import timeit
import line_profiler
import memory_profiler


geo_jsons = {
  "km2_26": {
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
              77.07115173339844,
              28.47804691199713
            ],
            [
              77.05741882324219,
              28.467936776194872
            ],
            [
              77.05707550048828,
              28.4433364363651
            ],
            [
              77.07475662231444,
              28.43050576788437
            ],
            [
              77.10514068603516,
              28.431713426539677
            ],
            [
              77.12196350097656,
              28.449222928177342
            ],
            [
              77.10891723632812,
              28.46733315539307
            ],
            [
              77.09243774414062,
              28.481064675455944
            ],
            [
              77.07115173339844,
              28.47804691199713
            ]
          ]
        ]
      }
    }
  ]
},
"km2_50": {
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
              77.06119537353516,
              28.49600133462104
            ],
            [
              77.02875137329102,
              28.46914400745396
            ],
            [
              77.0694351196289,
              28.42341049498704
            ],
            [
              77.1324348449707,
              28.44394019419311
            ],
            [
              77.1188735961914,
              28.49011744843003
            ],
            [
              77.06119537353516,
              28.49600133462104
            ]
          ]
        ]
      }
    }
  ]
},
"km2_100": {
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
              77.02377319335936,
              28.559496241467098
            ],
            [
              77.02377319335936,
              28.561607053766586
            ],
            [
              76.95785522460938,
              28.478348692223165
            ],
            [
              77.02720642089844,
              28.437902460838288
            ],
            [
              77.10514068603516,
              28.51847777650959
            ],
            [
              77.02377319335936,
              28.559496241467098
            ]
          ]
        ]
      }
    }
  ]
},
"km2_250": {
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
              76.99871063232422,
              28.544719370308737
            ],
            [
              76.90223693847656,
              28.453901700762646
            ],
            [
              77.03922271728514,
              28.360286940947283
            ],
            [
              77.15938568115234,
              28.472614720490967
            ],
            [
              76.99871063232422,
              28.544719370308737
            ]
          ]
        ]
      }
    }
  ]
},
"km2_600": {
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
              76.96609497070312,
              28.60743139267596
            ],
            [
              76.86172485351562,
              28.50369515241441
            ],
            [
              76.93588256835938,
              28.38415145897281
            ],
            [
              77.08145141601562,
              28.370860490997323
            ],
            [
              77.18719482421874,
              28.438506249680675
            ],
            [
              77.16659545898438,
              28.582109884356534
            ],
            [
              76.96609497070312,
              28.60743139267596
            ]
          ]
        ]
      }
    }
  ]
},
"km2_960": {
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
              76.981201171875,
              28.627925287618567
            ],
            [
              76.8548583984375,
              28.521796040000677
            ],
            [
              76.96746826171875,
              28.36361017019959
            ],
            [
              77.17483520507812,
              28.34789944257093
            ],
            [
              77.2943115234375,
              28.472312923883393
            ],
            [
              77.18307495117188,
              28.63395214251842
            ],
            [
              76.981201171875,
              28.627925287618567
            ]
          ]
        ]
      }
    }
  ]
}}


# In[14]:



# decision_data = []
# for key, value in geo_jsons.items():
#     start_time = time.time()

#     h3_polygon = h3.polyfill(value.get('features')[0]['geometry'], 12 , geo_json_conformant=True)
#     polyfill_time = time.time() - start_time

#     compact_start_time = time.time()
#     h3_compact_polygon = h3.compact(h3_polygon)
#     compact_time = time.time() - compact_start_time
#     total_time = time.time() - start_time
#     polyfill_cell_count = len(h3_polygon)
#     compact_cell_count = len(h3_compact_polygon)

#     decision_data.append([key, start_time, polyfill_time, compact_time, total_time, polyfill_cell_count, compact_cell_count])

# # dataframe = pd.DataFrame(decision_data, columns=['Area', 'Start Time ', 'Polyfill Time', 'Compact Time', 'Total Time', 'Polyfill Cell Count', 'Compact Cell Count'])


# # In[15]:


def func1():
    decision_data = []
    for key, value in geo_jsons.items():
        start_time = time.time()

        h3_polygon = h3.polyfill(value.get('features')[0]['geometry'], 12 , geo_json_conformant=True)
        polyfill_time = time.time() - start_time

        compact_start_time = time.time()
        h3_compact_polygon = h3.compact(h3_polygon)
        compact_time = time.time() - compact_start_time
        total_time = time.time() - start_time
        polyfill_cell_count = len(h3_polygon)
        compact_cell_count = len(h3_compact_polygon)

        decision_data.append([key, start_time, polyfill_time, compact_time, total_time, polyfill_cell_count, compact_cell_count])


