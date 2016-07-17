#--------------#------------------#
# onGEO@MSU - Python Geoprocessing
# Lesson 3 - Data Types
# -------------#------------------#
# Numbers
a = 7
b = 7.0
print type(a)
print type(b)

# Strings
y ='geoprocessing'
print y[-1]  # This is indexing, it returns the last character, i.e. 'g'

print y[0:3]  # This is slicing, it returns characters from position 0 (included) to 3 (excluded), i.e. 'geo'

x = 'arcgis'
print x[1]          # this will print r
print len(x)        # this will print 6
print x + ' arcpy'  # this will print arcgis arcpy

# Lists
land_types = ['pasture', 'water', 'farmland', 'urban']
print land_types[1]          # water
print len(land_types)        # 4
print land_types[-1]         # urban
# note that [-1] takes the last item in a list

# Tuples
tuple1 = (1, 2, 'string', 4)
print tuple1[0:3]

# Dictionaries
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
   print key, 'corresponds to', d[key]
