import arcpy
arcpy.env.workspace = "__________"
arcpy.env.overwriteoutput = True
fcList = arcpy.ListFeatureClasses("")
# Make a for loop
__ fc _ fcList:
    # set up an if / else statement
    __ fc _____ "Lakes" _____ fc _____ "Streams"_
        print "Some of our data are Lakes and Streams."
    # use an elif statement
    ____ fc _____ "Forest" _____ fc == "Wilderness"_
        print "Some of our data are Forest and Wilderness." 
    # finish the conditionals by using an else: statement
    _____                                   
        _____ "Some data are neither Lakes, Streams, Forest, or Wilderness"
