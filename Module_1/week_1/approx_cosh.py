import math 
def approx_cosh(x, n):
    x = math.radians(x)
    cosh_x = 0
    for i in range(n):
        cosh_x += (x**(2*i))/math.factorial(2*i)
    return cosh_x

if __name__=="main":
    assert math.isclose(round(approx_cosh(x=1, n=10), 2), 1.54, rel_tol=1e-09, abs_tol=1e-09)
    print(round(approx_cosh(x=3.14, n=10), 2))