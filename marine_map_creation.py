# Creation of map

# First lets import the functions and modules we need to create the map

import cartopy.crs as ccrs
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
from cartopy.feature import ShapelyFeature
import matplotlib.patches as mpatches
import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point


# Loading the data
outline = gpd.read_file('project data/IRL_adm/IRL_adm0.shp')  # outline of Ireland
counties = gpd.read_file('project data/Counties_-_National_Statutory_Boundaries_-_2019/Counties___Ungen_2019.shp')  # counties boundaries
marine_eez = gpd.read_file('project data/Designated_Maritime_Boundary_Continental_Shelf/Designated_Maritime_Boundary_Continental_Shelf.shp')  # marine exclusive zone
ni_mpa = gpd.read_file('project data/Marine_Protected_Areas_MPAs_within_Northern_Ireland_s_marine_plan_extent/Marine_Protected_Areas_within_Marine_Plan_Extent.shp')  # Northern ireland MPA
irish_sea_mpa = gpd.read_file('project data/Marine_Protected_Area_UK/Marine_Protected_Area_UK.shp')  # irish sea MPA
dredge_fishing = gpd.read_file('project data/Dredge_Fishing/Dredge_Fishing.shp')  # Dredge fishing areas
bottom_trawl_fishing = gpd.read_file('project data/Bottom_Trawl_Fishing/Bottom_Trawl_Fishing.shp')   # Bottom trawl areas

# Define the map projection
proj = ccrs.OSGB()

# creating the map
myFig = plt.figure(figsize=(10, 10))  # create a figure of size 10x10 (inches)
myCRS = ccrs.UTM(29)  # create a reference system to transform data
ax = plt.axes(projection=ccrs.Mercator())   # create an axes object in the figure,

# adding features, outline of Ireland
outline_feature = ShapelyFeature(outline['geometry'], myCRS, edgecolor='green', facecolor='burlywood')
xmin, ymin, xmax, ymax = outline.total_bounds
ax.add_feature(outline_feature)
outline = outline.to_crs("EPSG:2157")   # CRS relevant to Ireland

# using the boundary of the shapefile features, zoom the map to our area of interest
ax.set_extent([xmin-5000, xmax+5000, ymin-5000, ymax+5000], crs=myCRS)


# Adding counties to map
counties_feature = ShapelyFeature(counties['geometry'], myCRS, edgecolor='black', facecolor='lightpink', linewidth=0.5)
ax.add_feature(counties_feature)

# Add marine economic exclusive zone boundary to map
eez_feature = ShapelyFeature(marine_eez['geometry'], myCRS, edgecolor='cadetblue', linewidth=2)
ax.add_feature(eez_feature)

# Add Northern Ireland marine protected areas (MPA) to map
nimpa_feature = ShapelyFeature(ni_mpa['geometry'], myCRS, edgecolor='magenta', facecolor='magenta')
ax.add_feature(nimpa_feature)

# Add Irish Sea marine protected areas to map
irishmpa_feature = ShapelyFeature(irish_sea_mpa['geometry'], myCRS, edgecolor='hotpink', facecolor='hotpink')
ax.add_feature(irishmpa_feature)

# Add areas of dredge fishing to map
dredgefish_feature = ShapelyFeature(dredge_fishing['geometry'], myCRS, edgecolor='orange', facecolor='orange')
ax.add_feature(dredgefish_feature)

# Add areas of bottom trawling fishing to map
trawlfish_feature = ShapelyFeature(bottom_trawl_fishing['geometry'], myCRS, edgecolor='coral', facecolor='coral')
ax.add_feature(dredgefish_feature)

plt.show()

# Create map legend
# generate matplotlib handles to create a legend of the features we put in our map.
def generate_handles(labels, colors, edge='k', alpha=1):
    lc = len(colors)  # get the length of the color list
    handles = []
    for i in range(len(labels)):
        handles.append(mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[i % lc], edgecolor=edge, alpha=alpha))
    return handles

# Create map labels
ax.set_title('Map of Ireland Marine Protected Areas and Fishing Zones'), ax.set_xlabel('Longitude'), ax.set_ylabel('Latitude')

# adding grid lines
gridlines = ax.gridlines(draw_labels=True,
                         xlocs=[-7.5, -6.5, -5.5, -4.5, -3.5],
                         ylocs=[10, 11, 9, 8, 7, 6, 5, 4])
gridlines.left_labels = True # turn off the left-side labels
gridlines.right_labels = False #turn off the right side labels
gridlines.bottom_labels = False # turn off the bottom labels


# Set the extent of the map to zoom in on Ireland
ax.set_extent([-10, -5, 51.5, 55], crs=ccrs.PlateCarree())


plt.show()