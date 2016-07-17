#--------------#------------------#
# onGEO@MSU - Python Geoprocessing
# Lesson 4 - Duplicate Invasives
# -------------#------------------#
# Description: Create 3 empty Feature Classes
# using the Invasive_plants layer as a template
# for the purpose of testing out new data

## Section 1. ##
# Import system modules
import arcpy
arcpy.env.overwriteOutput = True

## Section 2. ##
# Set workspace
arcpy.env.workspace = "D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb"

## Section 3. ##
# Use the Describe function to get a SpatialReference object
# Set parameters for the CreateFeatureclass_management function
spatial_reference = arcpy.Describe("Invasive_plants").spatialReference
out_path = arcpy.env.workspace
geometry_type = "POINT"
template = "Invasive_plants"
has_m = "DISABLED"
has_z = "DISABLED"

## Section 4. ##
# Set up while loop
n = 1
while n < 4:
    out_name = "out{0}".format(n)
    ## Section 5. ##
    # Execute CreateFeatureclass_management and update n
    arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference)
    print "Shapefile {0} creation complete.".format(n)
    n += 1

## Section 6. ##
# Print a final message
print "Script complete"
