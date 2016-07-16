'''Only mutable objects support methods that change the object in place,
such as reassignment of a sequence slice, which will work for lists,
but raise an error for tuples and strings.
It is important to understand that variables in Python
are really just references to objects in memory.'''

# If you assign an object to a variable as below
a = 1
s = 'abc'
l = ['a string', 456, ('a', 'tuple', 'inside', 'a', 'list')]
print 'a is originally {0}'.format(a)
print 's is originally {0}'.format(s)
print 'l is originally {0}'.format(l)
# all you really do is make this variable (a, s, or l)
# point to the object (1, 'abc', ['a string', 456, ('a', 'tuple', 'inside', 'a', 'list')]),
# which is kept somewhere in memory, as a convenient way of accessing it. If you reassign a variable as below

a = 7
s = 'xyz'
l = ['a simpler list', 99, 10]
print 'a has been changed to {0}'.format(a)
print 's has been changed to {0}'.format(s)
print 'l has been changed to {0}'.format(l)

# you make the variable point to a different, newly created object.
# As stated above, only mutable objects can be changed in place
# (l[0] = 1 is ok in our example, but s[0] = 'a' raises an error).

l[0] = 1
print 'l is now {0}'.format(l)
print "s[0] = 'a' will throw an error"
