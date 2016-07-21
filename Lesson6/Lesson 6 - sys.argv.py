import os
import sys
import arcpy
arcpy.env.overwriteOutput = True

# Set the input workspace, get the feature class name to copy
# and the output location.
arcpy.env.workspace = sys.argv[1]
in_featureclass = sys.argv[2]
out_workspace = sys.argv[3]

in_fc = os.path.join(arcpy.env.workspace, in_featureclass)

print "We are copying {}".format(in_fc)

# Copy feature class to output location
arcpy.CopyFeatures_management(in_fc, out_workspace)

print "Successfully copied Feature Class '{}' to directory {}".format(os.path.basename(in_fc),out_workspace)
