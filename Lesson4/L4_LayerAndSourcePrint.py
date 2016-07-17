#--------------#------------------#
# onGEO@MSU - Python Geoprocessing
# Lesson 4 - Layer and Source Print
# -------------#------------------#
# This script loops through a geodatabase and
# prints the Name and Data Source of each Layer
import arcpy
arcpy.env.workspace = "D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb"
fcList = arcpy.ListFeatureClasses("")
for fc in fcList:
    desc = arcpy.Describe(fc)
        print "Layer name: {}".format(desc.name)
        print "Layer data source: {}".format(desc.catalogPath)
