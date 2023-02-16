import pytest
from triangle.triangle import Triangle


@pytest.fixture()
def s_triangle():
    s_t = Triangle(3, 4, 5)
    yield s_t
    del s_t


@pytest.fixture()
def common_triangle():
    common_tr = Triangle(4, 4, 5)
    yield common_tr
    del common_tr


@pytest.fixture(params=[(3, 3, 3), (4, 4, 4), (8, 8, 8)])
def equilateral_triangle(request):
    eguil_trian = Triangle(request.param[0], request.param[1], request.param[2])
    yield eguil_trian
    del eguil_trian
