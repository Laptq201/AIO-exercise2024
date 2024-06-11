import math
def approx_cos(x, n):
    x = math.radians(x)
    cos_x = 0
    for i in range(n):
        cos_x += ((-1)**i)*(x**(2*i))/math.factorial(2*i)
    return cos_x

if __name__=="main":
    assert math.isclose(round(approx_cos(x=1, n=10), 2), 0.54, rel_tol=1e-09, abs_tol=1e-09)
    print(round(approx_cos(x=3.14, n=10), 2))