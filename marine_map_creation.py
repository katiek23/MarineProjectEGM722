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
import folium



# generate matplotlib handles to create a legend of the features we put in our map.
def generate_handles(labels, colors, edge='k', alpha=1):
    lc = len(colors)  # get the length of the color list
    handles = []
    for i in range(len(labels)):
        handles.append(mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[i % lc], edgecolor=edge, alpha=alpha))
    return handles

# create a scale bar of length 20 km in the upper right corner of the map
def scale_bar(ax, location=(0.92, 0.95)):
    x0, x1, y0, y1 = ax.get_extent()
    sbx = x0 + (x1 - x0) * location[0]
    sby = y0 + (y1 - y0) * location[1]

    ax.plot([sbx, sbx - 20000], [sby, sby], color='k', linewidth=9, transform=ax.projection)
    ax.plot([sbx, sbx - 10000], [sby, sby], color='k', linewidth=6, transform=ax.projection)
    ax.plot([sbx-10000, sbx - 20000], [sby, sby], color='w', linewidth=6, transform=ax.projection)

    ax.text(sbx, sby-4500, '20 km', transform=ax.projection, fontsize=8)
    ax.text(sbx-12500, sby-4500, '10 km', transform=ax.projection, fontsize=8)
    ax.text(sbx-24500, sby-4500, '0 km', transform=ax.projection, fontsize=8)


# Loading the data
outline = gpd.read_file('project data/OSNI_Open_Data_-_Largescale_Boundaries_-_NI_Outline/OSNI_Open_Data_-_Largescale_Boundaries_-_NI_Outline.shp')  # outline of Northern Ireland
counties = gpd.read_file('project data/Counties_-_National_Statutory_Boundaries_-_2019/Counties___Ungen_2019.shp')  # counties boundaries
seagrass_habitat = gpd.read_file('project data/Subtidal_and_Intertidal_Seagrass_Beds/SubtidalAndIntertidalSeagrassBedsNI.shp')  # Seagrass habitats
ni_mpa = gpd.read_file('project data/Marine_Protected_Areas_(MPAs)_within_Northern_Ireland_s_marine_plan_extent/Marine_Protected_Areas_within_Marine_Plan_Extent.shp')  # Northern ireland MPA
nursery_grounds = gpd.read_file('project data/spawning_grounds_1998_superceded/nursery_grounds_1998_superceded.shp')  # Fish nursery grounds
fishing_activity = gpd.read_file('project data/Recordset_8763/Recordset_8763Polygon.shp')  # Inshore fishing activity in  Irish Sea

# creating the map
myFig = plt.figure(figsize=(9, 9))  # create a figure of size 10x10 (inches)
myCRS = ccrs.UTM(29)  # create a reference system to transform data
ax = plt.axes(projection=myCRS)   # create an axes object in the figure,

# adding features, outline of Northern Ireland
outline_feature = ShapelyFeature(outline['geometry'], myCRS, edgecolor='green', facecolor='burlywood')
xmin, ymin, xmax, ymax = outline.total_bounds
ax.add_feature(outline_feature)
outline = outline.to_crs("EPSG:2157")   # CRS relevant to Ireland

# using the boundary of the shapefile features, zoom the map to our area of interest
ax.set_extent([xmin-10, xmax+10, ymin-10, ymax+10], crs=myCRS)

# get the number of unique fish species we have in each of the nursery grounds in the dataset
num_species = len(nursery_grounds.Species.unique())
print('Number of unique features: {}'.format(num_species))

species_colors = ['seagreen', 'mediumspringgreen', 'lightseagreen', 'mediumseagreen', 'mediumaquamarine', 'mediumturquoise',
                  'aquamarine', 'teal', 'darkcyan', 'cyan', 'g', 'lightgreen', 'palegreen', 'turquoise']

# get a list of unique species names within fish nursery grounds
species_names = list(nursery_grounds.Species.unique())
species_names.sort() # sort the counties alphabetically by name

# add fish nursery ground areas to the map using the colors picked above

for ii, name in enumerate(species_names):
    feat = ShapelyFeature(nursery_grounds.loc[nursery_grounds['Species'] == name, 'geometry'],
                          myCRS, edgecolor='k', facecolor=species_colors[ii], linewidth=1, alpha=0.25)
    ax.add_feature(feat)

# Adding counties to map
counties_feature = ShapelyFeature(counties['geometry'], myCRS, edgecolor='black', facecolor='lightpink', linewidth=0.5)
ax.add_feature(counties_feature)

# Add seagrass beds and habitat to map
seagrass_feature = ShapelyFeature(seagrass_habitat['geometry'], myCRS, edgecolor='yellow', facecolor='yellow',  linewidth=2)
ax.add_feature(seagrass_feature)

# Add Northern Ireland marine protected areas (MPA) to map
nimpa_feature = ShapelyFeature(ni_mpa['geometry'], myCRS, edgecolor='magenta', facecolor='magenta')
ax.add_feature(nimpa_feature)

# Add areas of inshore fishing activity to map
inshorefishing_feature = ShapelyFeature(fishing_activity['geometry'], myCRS, edgecolor='orange', facecolor='orange')
ax.add_feature(inshorefishing_feature)


# Create map legend

# generate matplotlib handles to create a legend of the features we put in our map.

species_handles = generate_handles(nursery_grounds.Species.unique(), species_colors, alpha=0.25)

county_handles = generate_handles(['Counties'], ['pink'])
seagrass_handle = generate_handles(['Seagrass Habitat'], ['yellow'])
mpa_handle = generate_handles(['Marine Protected Areas'], ['magenta'])
fishing_handle = generate_handles(['Inshore Fishing Areas'], ['orange'])

# Create legend by combining all handles
handles = species_handles + county_handles + seagrass_handle + mpa_handle + fishing_handle
labels = ['Fish Nursery Grounds', 'Counties', 'Seagrass Habitat', 'Marine Protected Areas', 'Inshore Fishing Areas']
leg = ax.legend(handles, labels, title='Legend', title_fontsize=12,
                 fontsize=10, loc='upper left', frameon=True, framealpha=1)

# Create map labels
ax.set_title('Map of Irish Sea Marine Protected Areas and Fishing Zones'), ax.set_xlabel('Longitude'), ax.set_ylabel('Latitude')

# adding grid lines
gridlines = ax.gridlines(draw_labels=True,
                         xlocs=[-7.5, -6.5, -5.5, -4.5, -3.5],
                         ylocs=[10, 11, 9, 8, 7, 6, 5, 4])
gridlines.left_labels = True  # turn off the left-side labels
gridlines.right_labels = False  # turn off the right side labels
gridlines.bottom_labels = False  # turn off the bottom labels

# Show completed map
plt.show()

# Use this code below when you are ready to save as a .png file!
myFig.savefig('map.png', bbox_inches='tight', dpi=300)
