# test_math.py

from my_math import abs, cube_volume, cylinder_volume

def test_abs():
    # Typical cases
    assert abs(5) == 5
    assert abs(-5) == 5

    # Edge cases
    assert abs(0) == 0
    assert abs(3.14) == 3.14

    # Invalid input
    try:
        abs("hello")
        assert False, "Expected TypeError for string input"
    except TypeError:
        pass

    try:
        abs(None)
        assert False, "Expected TypeError for None input"
    except TypeError:
        pass


def test_cube_volume():
    # Typical case
    assert cube_volume(3) == 27

    # Edge case: zero
    assert cube_volume(0) == 0

    # Negative value (mathematically acceptable)
    assert cube_volume(-2) == -8


def test_cylinder_volume():
    pi = 3.141592653589793

    # Typical case
    assert cylinder_volume(2, 5) == pi * 2 * 2 * 5

    # Edge case: zero radius or height
    assert cylinder_volume(0, 10) == 0
    assert cylinder_volume(3, 0) == 0

    # Negative values (mathematically allowed but unusual)
    assert cylinder_volume(-2, 5) == pi * (-2) * (-2) * 5


if __name__ == "__main__":
    test_abs()
    test_cube_volume()
    test_cylinder_volume()

    print("✅ All tests passed successfully!")
