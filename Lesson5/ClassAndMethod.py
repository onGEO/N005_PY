#--------------#------------------#
# onGEO@MSU - Python Geoprocessing
# Lesson 5 - Class and Method Example
# -------------#------------------#

class first_class:
    def a_method(self):
        print "You have just used the method, a_method, which is simply a member of the class, first_class "

c = first_class()
c.a_method() # Prints "You have just used a_method..."
