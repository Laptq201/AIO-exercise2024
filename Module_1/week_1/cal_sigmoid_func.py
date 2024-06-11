import math 
def calc_sig(x):
    return 1/(1 + math.exp(-x))

if __name__=="main":
    assert math.isclose(round(calc_sig(3), 2), 0.95, rel_tol=1e-09, abs_tol=1e-09)
    print (round(calc_sig (2), 2))