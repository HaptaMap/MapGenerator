#! /usr/bin/env python3

import prettymaps
import matplotlib.pyplot as plt
from matplotlib.artist import Artist


#MAP_TARGET="48.7292565,9.1118945"
MAP_TARGET="48.7303954,9.111095"
#MAP_TARGET="Vaihingen-Mitte"

MIN_TACTILE_SIZE=3

dilate=0

fig, ax = plt.subplots(figsize = (6, 6), constrained_layout = True)
fig.patch.set_facecolor('black')
ax.patch.set_facecolor('black')

def post(layers):
    print(layers)
    import pdb; pdb.set_trace()
    return layers

layers = prettymaps.plot(
    # Address:
    MAP_TARGET,
    # Plot geometries in a circle of radius:
    radius = 140, #vaihingen Mitte: 140
    # Matplotlib axis
    ax = ax,
    # Which OpenStreetMap layers to plot and their parameters:
    layers = {
            # Perimeter (in this case, a circle)
            'perimeter': {
                'circle': False,
                'dilate': 0,
            },
            # Streets and their widths
            'streets': {
                'width': {
                    'motorway': 5,
                    'trunk': 5,
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'residential': 3,
                    'service': 2,
                    'unclassified': 2,
                    'pedestrian': 2,
                    'footway': 1,
                    'cycleway': 1,
                    'path': 4,
                    'sidewalk': 4,
                    'track': 4,
                },
                'circle': False,
                'dilate': dilate,
            },
            # Other layers:
            #   Specify a name (for example, 'building') and which OpenStreetMap tags to fetch
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False, 'circle': False, 'dilate': dilate,},
            #'water': {'tags': {'natural': ['water', 'bay']}, 'circle': False, 'dilate': dilate,},
            'tactile': {
                'tags': { 'information': 'tactile_map', 'traffic_signals:sound': True, 'traffic_signals:vibration': True, 'tactile_paving': True,}, 
                'union': True, 'circle': False, 'dilate': dilate,},
            'ped': {'tags': {'highway': 'pedestrian', }, 'circle': False, 'dilate': dilate,},
            #'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}, 'circle': False, 'dilate': dilate,},
            #'forest': {'tags': {'landuse': 'forest'}, 'circle': False, 'dilate': dilate,},
            #'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}, 'circle': False, 'dilate': dilate,},
            
        },
        # drawing_kwargs:
        #   Reference a name previously defined in the 'layers' argument and specify matplotlib parameters to draw it
        drawing_kwargs = {
            'background': {'fc': '#000', 'ec': '#000', 'lw': 0, 'zorder': -2},
            'perimeter': {'fc': '#000', 'ec': '#000', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
            # 'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
            # 'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
            # 'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
            # 'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
            'streets': {'fc': '#888', 'ec': '#888', 'lw': 1},
            'ped': {'fc': '#888', 'ec': '#888', 'lw': 1},
            'building': {'fc': '#AAA', 'ec': '#AAA', 'lw': 1, 'zorder':0},
            # 'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
            'tactile': {'fc': '#FFF', 'ec': '#FFF', 'lw': 3, 'zorder': 5},
        },
        osm_credit = {'x': 0.0, 'y': 0.0, 'color': '#888'},
        rotation=0,
)

#import pdb; pdb.set_trace()
# xmin, ymin, xmax, ymax = layers['perimeter'].bounds
# dx, dy = xmax-xmin, ymax-ymin
# a = .2
# ax.set_xlim(xmin+a*dx, xmax-a*dx)
# ax.set_ylim(ymin+a*dy, ymax-a*dy)

#for poly in layers['tactile']
Artist.remove(fig.axes[0].figure.axes[0].texts[0])

plt.savefig("test_map.svg")
plt.savefig("test_map.png")
# plt.savefig("test_map_paths.svg")
# plt.savefig("test_map_paths.png")