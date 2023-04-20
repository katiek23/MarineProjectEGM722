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
counties= gpd.read_file('project data/Counties_-_National_Statutory_Boundaries_-_2019/Counties___Ungen_2019.shp')  #counties boundaries
marine_eez= gpd.read_file('project data/Designated_Maritime_Boundary_Continental_Shelf/Designated_Maritime_Boundary_Continental_Shelf.shp')# marine exclusive zone
ni_mpa= gpd.read_file('project data/Marine_Protected_Areas_MPAs_within_Northern_Ireland_s_marine_plan_extent/ Marine_Protected_Areas_within_Marine_Plan_Extent.shp')# Northern ireland MPA
irish_sea_mpa= gpd.read_file('project data/Marine_Protected_Area_UK/ Marine_Protected_Area_UK.shp') #irish sea MPA
dredge_fishing= gpd.read_file('project data/Dredge_Fishing/Dredge_Fishing.shp') # Dredge fishing areas
bottom_trawl_fishing= gpd.read_file( 'project data/Bottom_Trawl_Fishing/ Bottom_Trawl_Fishing.shp') # Bottom trawl areas
seagrass= gpd.read_csv(' project data/Subtidal_and_Intertidal_Seagrass_Beds.csv') #importing seagrass for conversion

 # convert seagrass database into points shapefile
seagrass['geometry'] = list(zip(seagrass['LongWGS84'], seagrass['LatWGS84']))
seagrass['geometry'] = seagrass['geometry'].apply(Point)
seagrassgdf: GeoDataFrame = gpd.GeoDataFrame(seagrass)
seagrassgdf.set_geometry('geometry')
seagrassgdf.set_crs("EPSG:4326", inplace=True) #sets the coordinate reference system to epsg:3857 WGS84 lat/lon
seagrassgdf.to_file('seagrass_dist.shp')

# Load new seagrass shapefile
seagrass_dist= gpd.read_file('seagrass_dist.shp')

# Define the map projection
proj = ccrs.OSGB()

#creating the map
myFig = plt.figure(figsize=(10, 10))  # create a figure of size 10x10 (inches)
myCRS = ccrs.UTM(29)  # create a reference system to transform data
ax = plt.axes(facecolor='lightblue', projection=ccrs.Mercator())   #create an axes object in the figure,
