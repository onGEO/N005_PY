#--------------#------------------#
# onGEO@MSU - Python Geoprocessing
# Lesson 7 - Water Buffer Tool
# -------------#------------------#
#
import arcpy
# Create List of feature classes to Buffer
bufferList = ["Lakes", "Streams"]
# Initialize a new Python list of feature classes to be Unioned together
unionList = []
for fc in bufferList:
    # Buffer each feature class and dissolve any overlapping polygons
    arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters", "", "ALL")
    # Add each buffer feature class to a list of feature classes to Union
    unionList.append(fc + "Buffer")
# Union the buffered featured classes
arcpy.Union_analysis(unionList, "WaterBuffers")
