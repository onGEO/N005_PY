# RenameMultipleFields.py
## Section 1. ##
import arcpy
# Set workspace environment to geodatabase
arcpy.env.workspace = r"D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb"

## Section 2. ##
# Loop through feature classes
fcList = arcpy.ListFeatureClasses() # get a list of feature classes
for fc in fcList:  # loop through feature classes
    if fc == "Roads_new": # find the new Roads feature class
        print "We are using Feature Class: {0}".format(fc)
        fieldList = arcpy.ListFields(fc)  # get a list of fields for the feature class

        ## Section 3. ##
        for field in fieldList: # loop through each field and alter the field name

        ## Section 4. ##
        ## Check if the field name equals one of the expected truncated versions. If so, run AlterField_Management and change the field name to something that makes sense.
            if field.name == 'ROUTE_NUMB':
                arcpy.AlterField_management(fc, field.name, "ROUTE_NUMBER", "ROUTE_NUMBER")
                print "- Altered field name: {0} to {1}".format(field.name, "ROUTE_NUMBER")
            elif field.name == 'Shape_Leng':
                arcpy.AlterField_management(fc, field.name, "Road_Length", "Road_Length")
                print "- Altered field name: {0} to {1}".format(field.name, "Road_Length")
            elif field.name == 'ROUTE_TYPE':
                arcpy.AlterField_management(fc, field.name, "ROUTE_TYPE_A", "ROUTE_TYPE_A")
                print "- Altered field name: {0} to {1}".format(field.name, "ROUTE_TYPE_A")
            elif field.name == 'ROUTE_TY_1':
                arcpy.AlterField_management(fc, field.name, "ROUTE_TYPE_B", "ROUTE_TYPE_B")
                print "- Altered field name: {0} to {1}".format(field.name, "ROUTE_TYPE_B")
            elif field.name == 'ROUTE_TY_2':
                arcpy.AlterField_management(fc, field.name, "ROUTE_TYPE_C", "ROUTE_TYPE_C")
                print "- Altered field name: {0} to {1}".format(field.name, "ROUTE_TYPE_C")
            elif field.name == 'DISTANCE_1':
                arcpy.AlterField_management(fc, field.name, "DISTANCE_DRIVEN", "DISTANCE_DRIVEN")
                print "- Altered field name: {0} to {1}".format(field.name, "DISTANCE_DRIVEN")
            else:
                print "Did not Alter Field Name: {0}".format(field.name)
    else:
        print "We are not using Feature Class: {0}".format(fc)
print "Script Complete"
