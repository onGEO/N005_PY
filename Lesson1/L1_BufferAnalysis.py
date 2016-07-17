#--------------#------------------#
# onGEO@MSU - Python Geoprocessing
# Lesson 1 - Buffer Analysis
# -------------#------------------#
# *** Only copy the line of code below! ***
# *** Do not copy any of the comments! ***

arcpy.Buffer_analysis("D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb\Lakes", "Lakes_buffer.shp", "2 miles", "OUTSIDE_ONLY", "ROUND", "ALL")
