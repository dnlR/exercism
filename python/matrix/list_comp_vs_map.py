def v1():
 return [int(x) for x in '8743-12083-15'.split('-')]

def v2():
 return map(int, '8743-12083-15'.split('-'))

import timeit
print("v1", timeit.Timer('v1()', 'from __main__ import v1').timeit(500000))
print("v2", timeit.Timer('v2()', 'from __main__ import v2').timeit(500000))