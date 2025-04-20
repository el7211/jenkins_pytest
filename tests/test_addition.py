import pytest

# 🔧 Fixture to provide multiple (a, b, c) tuples
@pytest.fixture(params=[
    (1, 2, 3),
    (5, 7, 12),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300)
])
def addition_data(request):
    return request.param

# 🧪 Test using the fixture
def test_addition(addition_data):
    a, b, expected = addition_data
    result = a + b
    print(f"Testing: {a} + {b} = {result} (expected: {expected})")
    assert result == expected
