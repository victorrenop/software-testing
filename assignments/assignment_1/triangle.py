class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_valid(self):
        if (
            self.side_a + self.side_b > self.side_c
            and self.side_a + self.side_c > self.side_b
            and self.side_b + self.side_c > self.side_a
        ):
            return True
        return False

    def classify_triangle(self):
        if self.side_a == self.side_b == self.side_c:
            return "Equilateral"
        elif (
            self.side_a == self.side_b
            or self.side_a == self.side_c
            or self.side_b == self.side_c
        ):
            return "Isosceles"
        return "Scalene"
