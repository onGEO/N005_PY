# PrintSpatialReference.py

# import modules
import arcpy

# Set workspace
arcpy.env.workspace = "D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb"

# Name the Feature Class we want to Describe
featureClass = "Lakes"

# Describe the feature class and get its spatial reference
desc = arcpy.Describe(featureClass)
spatialRef = desc.spatialReference

# Print the spatial reference name
print spatialRef.name
