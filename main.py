def abs(x):
    """Return the absolute value of `x`.

    Supports integers and floats. Raises `TypeError` for non-numeric inputs.

    This implementation does not use Python's `math` module or the built-in
    `abs` function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f"abs() expected int or float, got {type(x).__name__}")
    return x if x >= 0 else -x


def volume_of_cube(*sides):
    """Return the volume for a cube or rectangular prism.

    Usage:
    - `volume_of_cube(side)` returns volume of a cube (side**3).
    - `volume_of_cube(a, b, c)` returns volume of a rectangular prism (a*b*c).

    Accepts `int` and `float`. Raises `TypeError` for non-numeric inputs and
    `ValueError` for negative side lengths. Raises `TypeError` for an unsupported
    number of arguments.
    """
    if len(sides) == 1:
        side = sides[0]
        if not isinstance(side, (int, float)):
            raise TypeError(f"volume_of_cube() expected int or float, got {type(side).__name__}")
        if side < 0:
            raise ValueError("side length must be non-negative")
        return side * side * side

    if len(sides) == 3:
        a, b, c = sides
        for name, val in (('a', a), ('b', b), ('c', c)):
            if not isinstance(val, (int, float)):
                raise TypeError(f"volume_of_cube() expected numeric values, got {type(val).__name__} for {name}")
            if val < 0:
                raise ValueError("side lengths must be non-negative")
        return a * b * c

    raise TypeError("volume_of_cube() accepts either 1 or 3 numeric arguments")


if __name__ == "__main__":
    # Tests for abs()
    assert abs(5) == 5
    assert abs(-3) == 3
    assert abs(0) == 0
    assert abs(2.5) == 2.5
    assert abs(-2.5) == 2.5

    try:
        abs("foo")
    except TypeError:
        pass
    else:
        raise AssertionError("abs() did not raise TypeError for non-numeric input")

    # Tests for volume_of_cube()
    assert volume_of_cube(3) == 27
    assert volume_of_cube(0) == 0
    assert volume_of_cube(2.5) == 15.625

    # Three-argument usage (rectangular prism)
    assert volume_of_cube(2, 3, 4) == 24
    assert volume_of_cube(1.5, 2, 2) == 6.0

    try:
        volume_of_cube("a")
    except TypeError:
        pass
    else:
        raise AssertionError("volume_of_cube() did not raise TypeError for non-numeric input")

    try:
        volume_of_cube(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("volume_of_cube() did not raise ValueError for negative side")

    # Three-arg error cases
    try:
        volume_of_cube(1, -2, 3)
    except ValueError:
        pass
    else:
        raise AssertionError("volume_of_cube() did not raise ValueError for negative side in 3-arg call")

    try:
        volume_of_cube(1, 2)
    except TypeError:
        pass
    else:
        raise AssertionError("volume_of_cube() did not raise TypeError for wrong arg count")

    print("All tests passed")
def abs(x):
	"""Return the absolute value of `x`.

	Supports integers and floats. Raises `TypeError` for non-numeric inputs.

	This implementation does not use Python's `math` module or the built-in
	`abs` function.
	"""
	if not isinstance(x, (int, float)):
		raise TypeError(f"abs() expected int or float, got {type(x).__name__}")
	return x if x >= 0 else -x


if __name__ == "__main__":
	# Simple sanity checks
	assert abs(5) == 5
	assert abs(-3) == 3
	assert abs(0) == 0
	assert abs(2.5) == 2.5
	assert abs(-2.5) == 2.5

	# Verify TypeError is raised for non-numeric input
	try:
		abs("foo")
	except TypeError:
		pass
	else:
		raise AssertionError("abs() did not raise TypeError for non-numeric input")

	print("All tests passed")

