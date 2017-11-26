# Python2
import collections
edges = [[0,1,3],[0,2,3],[0,3,3],[1,4,3]]
neighbors = collections.defaultdict(list)

for k, v, q in edges:
    print k, v, q

# 0 1 3
# 0 2 3
# 0 3 3
# 1 4 3

# traditional way
for i in xrange(len(edges)):
    for j in xrange(len(edges[0])):
        print edges[i][j],

# 0 1 3 0 2 3 0 3 3 1 4 3
