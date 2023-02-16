from triangle.triangle import Triangle
import pytest


class TestTrianglePtest:

    def test_triangle_perimetr(self):
        first = Triangle(4, 4, 5)
        assert first.perimetr() == 13

    def test_square(self, s_triangle):
        first = s_triangle
        assert first.square() == 6

    def test_triangle_ne(self, common_triangle):
        first = common_triangle
        second = Triangle(5, 6, 5)
        assert first != second

    def test_triangle_lt(self, common_triangle):
        first = common_triangle
        second = Triangle(9, 10, 11)
        assert first.perimetr() < second.perimetr()

    def test_triangle_gt(self, common_triangle):
        first = Triangle(10, 10, 10)
        second = common_triangle
        assert first.perimetr() > second.perimetr()

    @pytest.mark.parametrize("a, b, c,",
                             [(4, 4, 5), (10, 8, 10)])
    def test_triangle_le(self, a, b, c):
        first = Triangle(a, b, c)
        second = Triangle(10, 8, 10)
        assert first.perimetr() <= second.perimetr()

    @pytest.mark.parametrize("a, b, c,",
                             [(2, 8, 9), (5, 6, 7)])
    def test_triangle_ge(self, a, b, c):
        first = Triangle(a, b, c)
        second = Triangle(5, 6, 7)
        assert first.perimetr() >= second.perimetr()

    def test_triangle_corners(self, common_triangle):
        first = common_triangle
        second = Triangle(8, 8, 10)
        assert bool(first.with_same_corners(second)) is True

    @pytest.mark.parametrize("a, b, c,",
                             [(3, 4, 5), (5, 12, 13)])
    def test_right_angled(self, a, b, c, ):
        second = Triangle(a, b, c)
        assert bool(second.is_right_angled()) is True

    def test_equilateral_triangle(self, equilateral_triangle):
        assert bool(equilateral_triangle.is_right_triangle()) is True

    def test_isosceles_triangle(self, common_triangle):
        first = common_triangle
        assert bool(first.two_sides_eq()) is True
