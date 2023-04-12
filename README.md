# MarineProjectEGM722
**EGM722 Python Coding Project: Cetacean sightings around the Irish Coast**

Casual cetacan sightings data provided by the Irish Whale and Dolphin group (IWDG).
Step 1: creates a map with locations of sightings
Step 2: provides insight into Marine Protected Areas and Fishing activity in the area

This project aims to explore and plot cetacean (whale, dolphin, porpoise) sightings around the Irish Coast. Further, 
comparison to fishing activity can help determine whether an overlap in their distribution exists and whether this could have 
negative consequences for population health.

Thank you to the IWDG who kindly sent me this data. Their website can be found at [Irish Whale and Dolphin Group] (https://iwdg.ie) 
If you have any queries regarding this project, please contact Kerr-K22@ulster.ac.uk 

**Installation and Set Up instructions**

The following code has been designed to be run in Integrated Development Environment (IDE) was created in PyCharm. 
It is therefore suggested that PyCharm Community Edition is used to run the code as it has not been tested across other
environments.
The code, relevant data files, dependencies for installation and repository can be accessed here: [katiek23 repository] (https://github.com/katiek23/MarineProjectEGM722).
The dependencies for installation can also be viewed below:

**Marine_environment.yml file**
name: marineproject_env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - geopandas
  - cartopy
  - notebook
  - rasterio
  - pyepsg
  - folium
  
 **Recommended step-by-step guide for running code**
 
 1. Fork the repository [katiek23] (https://github.com/katiek23/MarineProjectEGM722) to create a copy on your GitHub Account.
 2. Clone the copy to GitHub Desktop
 3. Using Anaconda Navigator, create a new environment with the relevant title (eg. marine), using the marine_environment.yml file provided in the GitHub Repository.
 4.Follow through to the new environment (marine) and install PyCharm (community edition).
 5. In PyCharm, open the python script , Marine_map_creation. Once open, click where it says “Python 3.9” in the bottom right of the corner, click ‘Add interpreter’, then ‘Conda environment’, and then select ‘Existing environment’, and ensure the new conda environment is navigated to.
6. Then click ‘Add configuration’ and add the path to the script you are trying to run, and ensure “Python interpreter” is set to the correct environment
7. You should now be able to run the python scripts. 
 
