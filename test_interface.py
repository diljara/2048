import pytest
from interface import normalize, denormalize, get_nice_gradient


def test_normalize():
    color = (255, 128, 0)
    normalized = normalize(color)
    assert normalized[0] == pytest.approx(1.0)
    assert normalized[1] == pytest.approx(128/255)
    assert normalized[2] == pytest.approx(0.0)

def test_denormalize():
    color = (1.0, 0.5, 0.0)
    denormalized = denormalize(color)
    assert denormalized[0] == 255
    assert denormalized[1] == 127
    assert denormalized[2] == 0

@pytest.mark.parametrize("original", [
    (200, 100, 50),
    (0, 0, 0),
    (255, 255, 255),
    (128, 64, 192),
])
def test_normalize_denormalize_roundtrip(original):
    result = denormalize(normalize(original))
    for i in range(3):
        assert abs(result[i] - original[i]) <= 1

@pytest.mark.parametrize("N,expected_length", [
    (1, 1),
    (10, 10),
    (100, 100),
])
def test_get_nice_gradient_length(N, expected_length):
    gradient = get_nice_gradient(N)
    assert len(gradient) == expected_length

def test_get_nice_gradient_valid_colors():
    gradient = get_nice_gradient(20)

    for color in gradient:
        assert len(color) == 3
        for component in color:
            assert 0 <= component <= 255
