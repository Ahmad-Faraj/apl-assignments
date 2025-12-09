class Vector3D:
def __init__(self, x, y, z):
self.x, self.y, self.z = x, y, z
def __add__(self, other):
def __sub__(self, other):
def __mul__(self, other):
# Dot product: x1*x2 + y1*y2 + z1*z2
def __repr__(self):
# Test
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
print(f"Add: {v1 + v2}")
print(f"Sub: {v1 - v2}")
print(f"Dot: {v1 * v2}")