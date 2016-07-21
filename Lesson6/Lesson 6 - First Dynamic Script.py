#--------------#------------------#
# onGEO@MSU - Python Geoprocessing
# Lesson 6 - First Dynamic Script
# -------------#------------------#

# Description: A short script which demonstrates dynamic user input with ArcPy
#
# Section 1.
import os
import arcpy
arcpy.env.overwriteOutput = True

# Section 2.
# Set the input workspace, get the feature class name to copy
# and the output location.
arcpy.env.workspace = arcpy.GetParameterAsText(0)
in_featureclass = arcpy.GetParameterAsText(1)
out_workspace = arcpy.GetParameterAsText(2)

# Section 3.
in_fc = os.path.join(arcpy.env.workspace, in_featureclass)
print "We are copying {}".format(in_fc)

# Section 4.
# Copy feature class to output location
arcpy.CopyFeatures_management(in_fc, out_workspace)

print "Successfully copied Feature Class '{}' to directory {}".format(os.path.basename(in_fc),out_workspace)
