# Name: PrintFCnamesToFile.py
# Description: Loops through a list of Feature Classes
# and saves Layer names to a text file

## Section 1. ##
# Load Modules
# Set Workspace
import arcpy
import os
arcpy.env.overwriteOutput = True

# Set the workspace for the ListFeatureClass function
arcpy.env.workspace = "D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb"

## Section 2. ##
# Use the ListFeatureClasses function to return a list of all fc's in the gdb:
fcList = arcpy.ListFeatureClasses()

## Section 3. ##
# Write the name of the current fc in text file:
txtFile = open(r"D:\Classes\ONGEO\N005_PY\Course_Materials\Results\FeatureClassList.txt","w")
for fc in fcList:
    print fc

## Section 4. ##
    # Write messages to a Text File
    txtFile.write(fc)
    txtFile.write (os.linesep)

## Section 5. ##
# close text file
txtFile.close()

## Section 6. ##
print "done"
