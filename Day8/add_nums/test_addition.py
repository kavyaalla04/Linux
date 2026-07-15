from addition import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zeros():
    assert add(0, 5) ==5

def test_add_pandn():
    assert add(-2, 3) == 1

def test_add_floats():
    assert add(2.5, 3.1) == 5.6

def test_subtract_positive_numbers():
    from addition import subtract
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    from addition import subtract
    assert subtract(-5, -3) == -2

def test_subtract_zeros():
    from addition import subtract
    assert subtract(0, 0) == 0

def multiply_positive_numbers():
    from addition import multiply
    assert multiply(2, 3) == 6

def multiply_negative_numbers():
    from addition import multiply
    assert multiply(-2, -3) == 6

def multiply_zeros():
    from addition import multiply
    assert multiply(0, 5) == 0

def divide_positive_numbers():
    from addition import divide
    assert divide(6, 3) == 2

def divide_negative_numbers():
    from addition import divide
    assert divide(-6, -3) == 2

def divide_by_zero():
    from addition import divide
    try:
        divide(5, 0)
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivisionError"
