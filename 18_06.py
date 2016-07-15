# The gasup problem.
import collections

min_city_gas = collections.namedtuple('min_city_gas', ['c', 'g'])
mpg = 20

def find_ample_city(d, g):
    min_cg = min_city_gas(None, 0)
    min_g = 0
    for i in range(1, len(d)):
       min_g += g[i - 1] - d[i - 1]/mpg
       print min_g
       if min_g < min_cg.g:
           min_cg = min_city_gas(i, min_g)
    return min_cg.c

# Test.
d = [900, 600, 200, 400, 600, 200, 100]
g = [50, 20, 5, 30, 25, 10, 10]

print find_ample_city(d, g)
