#  generator function
# The performance improvement from the use of generators is the result of the lazy (on demand) generation of values, which translates to lower memory usage.
# Furthermore, we do not need to wait until all the elements have been generated before we start to use them. 

def nextValue(word):
    b = [1, -1]

    for i in xrange(len(word)):
        for j in b:
            yield i * j

for t in nextValue('hello'):
    print t,

# 0 0 1 -1 2 -2 3 -3 4 -4
