#--------------#------------------#
# onGEO@MSU - Python Geoprocessing
# Lesson 7 - Alter Tree Table
# -------------#------------------#
#
# Section 1
# import ArcPy and set the workspace
import arcpy
arcpy.env.workspace = "D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb"
# Set overwriteOutput to True
arcpy.env.overwriteOutput = True

# Section 2
# Create a new table named Trees
arcpy.CreateTable_management("D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb", "Trees")

# Add new attribute fields to the new table
# Add a text field named TREE_NAME
arcpy.AddField_management("Trees","TREE_NAME", "TEXT")
# Add a short integer field named COUNT
arcpy.AddField_management("Trees","COUNT", "SHORT")

# Section 3
# Set a variable named 'rows' equal to a new Insert Cursor using the 'Trees' table
# This will allow you to add or insert new rows into the table.
rows = arcpy.InsertCursor("Trees")

# Tell the cursor to create a new row into the table
row = rows.newRow()

# Set the TREE_NAME and COUNT attributes
row.TREE_NAME = "Quaking Aspen"
row.COUNT = 1650

# Insert the row into the table
rows.insertRow(row)

# Section 4
# Remove the two variables that reference the table
# This removes the locking on the table and allow it to be used in ArcGIS
del rows
del row
