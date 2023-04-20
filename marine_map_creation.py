# Creation of map

# First lets import the functions and modules we need to create the map

%matplotlib inline

import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
import cartopy.crs as ccrs
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from geopandas import GeoDataFrame
from shapely.geometry import Point

# Loading the data
outline= gpd.read_file('project data/Ireland_shapefile/ie_100km.shp')  #outline of Ireland

