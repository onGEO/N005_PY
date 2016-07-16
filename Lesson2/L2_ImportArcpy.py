# Importing ArcPy
#
import arcpy
arcpy.env.overwriteOutput = True


# Set the workspace environment and run Clip_analysis
arcpy.env.workspace = "D:\Classes\ONGEO\N005_PY\Course_Materials\Data\SanJuan.gdb"
arcpy.Clip_analysis("Forest", "Wilderness", "Forest_clip", "1.25")
