#--------------#------------------#
# onGEO@MSU - Python Geoprocessing
# Lesson 6 - Listing Fields
# -------------#------------------#
# Arguments: 
# D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb\Lakes
 
# import modules
import arcpy


# For each field in a feature class, print
#  the field name, type, and length.
fc = arcpy.GetParameterAsText(0) # Get user input for a feature class
fields = arcpy.ListFields(fc)
desc = arcpy.Describe(fc)


print "The name of the feature class is {0} \n It has fields: ".format(desc.name)

for field in fields:
    print "{0}, which is a type of {1} with a length of {2}".format(field.name, field.type, field.length)
