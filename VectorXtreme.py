class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __mul__(self, scalar):
        return Vector(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )

    def __eq__(self, other):
        return (self.x == other.x and
                self.y == other.y and
                self.z == other.z)

    def dot(self, other):
        return (self.x * other.x +
                self.y * other.y +
                self.z * other.z)

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def display(self):
        print(f"({self.x}, {self.y}, {self.z})")



x1, y1, z1 = map(int, input("Enter Vector 1 (x y z): ").split())
x2, y2, z2 = map(int, input("Enter Vector 2 (x y z): ").split())

v1 = Vector(x1, y1, z1)
v2 = Vector(x2, y2, z2)

print("\nAddition:")
(v1 + v2).display()

print("Subtraction:")
(v1 - v2).display()

print("Scalar Multiplication (v1 * 2):")
(v1 * 2).display()

print("Equality Check:", v1 == v2)

print("Dot Product:", v1.dot(v2))

print("Cross Product:")
v1.cross(v2).display()
