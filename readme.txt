FelipedelosH

Abstract:



Every project with geolocation hav a difierente codes to cities in the worls,
this program try to macth a diferente databases info ".csv" and generate a equals:

ProjectA.city_code = ProjectB.city_code

This program is create To macth a City+Country info 
Example: Turismoi > Netactica > Target.csv





How to RUN:

Install this libraries before to run:

import pandas as pd
from scipy import spatial
import pickle
from shapely.geometry import Point, Polygon
from decimal import Decimal



Steps to macth:

1 -> Load all info:
     * Turismoi
     * Netactica
     * Target
     * RESOURCES FOLDER

2 -> Add Geolocation Via Netactica:
     * This process its slowly

3.0 -> Init Tree Files.

3.1 -> Macth Turismoi via KdTree

     



