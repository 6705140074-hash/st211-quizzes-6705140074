import pytest
@pytest.mark.parameterize("X", [1, 2, 3])
@pytest.mark.parameterize("Y", [10, 20])
def test_combinations(x, y):
    assert x+ y > 0
    print(f"\n Testing x= {x}, y = {y}")