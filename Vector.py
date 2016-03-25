# 2D vector class with basic operations
# Offers dot product, unit vector, magnitude

class Vector(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	# Arithmetic operations
	def __add__(self, other):
		if type(other) == Vector:
			return Vector(self.x + other.x, self.y + other.y)
		else:
			raise TypeError("Can only add vectors to vectors")

	def __sub__(self, other):
		if type(other) == Vector:
			return Vector(self.x - other.x, self.y - other.y)
		else:
			raise TypeError("Can only subtract vectors with vectors")

	def __mul__(self, other):
		if type(other) == int or type(other) == float:
			return Vector(self.x * other, self.y * other)
		else:
			raise TypeError("Can only multiply vectors with scalars")

	def __div__(self, other):
		return self.__truediv__(other)

	def __truediv__(self, other):
		if type(other) == int or type(other) == float:
			return Vector(self.x / other, self.y / other)
		else:
			raise TypeError("Can only divide vectors by scalars")

	def __radd__(self, other):
		return other.__add__(self)

	def __rsub__(self, other):
		return other.__sub__(self)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __rdiv__(self, other):
		return other.__rtruediv__(self)

	def __rtruediv__(self, other):
		raise TypeError("Cannot divide by a vector")

	def __pos__(self): return self
	def __neg__(self): return Vector(-self.x, -self.y)

	# Output when printed
	def __repr__(self):
		return "<" + str(self.x) + ", " + str(self.y) + ">"

	# Vector operations
	def dot(self, other):
		return (self.x * other.x + self.y * other.y)

	def mag(self):
		return (self.x**2 + self.y**2) ** (1/2)

	def unit(self):
		return self / self.mag()


def dot(v1, v2):
	return v1.dot(v2)

def unit(v):
	return v.unit()

def mag(v):
	return v.mag()