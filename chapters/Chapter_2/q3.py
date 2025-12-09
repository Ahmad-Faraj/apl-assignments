class Point:
__slots__ = ('x', 'y')
def __init__(self, x, y):
self.x = x
self.y = y
p = Point(10, 20)
Explanation: When __slots__ is defined, Python does not create a __dict__ for instances.
Instead, it allocates a fixed amount of memory for only the specified attributes (x and y).