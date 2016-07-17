#--------------#------------------#
# onGEO@MSU - Python Geoprocessing
# Lesson 5 - Streams and Plants Buffer
# -------------#------------------#

import arcpy
# Set geoprocessing environments
arcpy.env.workspace = "D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb"
# Allow for overwriting
arcpy.env.overwriteOutput = True
# Create list of feature classes from SanJuan.gdb
fcList = arcpy.ListFeatureClasses()
# Create a for loop to buffer Streams and Invasive_plants
bufferList = []
for fc in fcList:
    if fc == "Streams" or fc == "Invasive_plants":
       arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters")
       bufferList.append(fc + " Buffer")

# Summarize the results of the geoprocessing
for item in bufferList:
    print "\n We have produced: {}".format(item)
