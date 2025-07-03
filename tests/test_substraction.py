import pytest

# 🔧 Fixture to provide multiple (a, b, c) tuples
@pytest.fixture(params=[
    (1, 2, -1),
    (5, 7, -2),
    (-1, 1, -2),
    (0, 0, 0),
    (100, 200, -100)
])
def substraction_data(request):
    return request.param

# 🧪 Test using the fixture
def test_substraction(substraction_data):
    a, b, expected = substraction_data
    result = a - b
    print(f"Testing: {a} - {b} = {result} (expected: {expected})")
    assert result == expected
