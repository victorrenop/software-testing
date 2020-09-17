from assignments.assignment_1.triangle import Triangle
import pytest


class TestTriangle:
    @pytest.mark.parametrize("a,b,c", [(1, 1, 1)])
    def test_valid_triangle(self, a, b, c):
        triangle = Triangle(a, b, c)

        assert triangle.is_valid() is True

    @pytest.mark.parametrize("a,b,c", [(1, 1, 2), (1, 2, 1), (2, 1, 1)])
    def test_invalid_triangle(self, a, b, c):
        triangle = Triangle(a, b, c)

        assert triangle.is_valid() is False

    @pytest.mark.parametrize("a,b,c", [(10, 10, 10)])
    def test_equilateral_triangle(self, a, b, c):
        triangle = Triangle(a, b, c)

        assert triangle.classify_triangle() == "Equilateral"

    @pytest.mark.parametrize("a,b,c", [(10, 10, 5), (10, 5, 10), (5, 10, 10)])
    def test_isosceles_triangle(self, a, b, c):
        triangle = Triangle(a, b, c)

        assert triangle.classify_triangle() == "Isosceles"

    @pytest.mark.parametrize("a,b,c", [(10, 7, 5)])
    def test_scalene_triangle(self, a, b, c):
        triangle = Triangle(a, b, c)

        assert triangle.classify_triangle() == "Scalene"
