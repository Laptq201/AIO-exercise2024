import math 
def is_number(n):
    try:
        int(n)
    except ValueError:
        return False
    return True



if __name__=="main":
    assert math.isclose(is_number(3), 1.0, rel_tol=1e-09, abs_tol=1e-09)
    assert math.isclose(is_number('-2a'), 0.0, rel_tol=1e-09, abs_tol=1e-09)
    print (is_number(1))
    print (is_number('n'))