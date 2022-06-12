from myapp import Calculator
def test_add():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.add() == x + y, "La suma tiene problemas"

def test_subtract():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.subtract() == x-y, "La resta no funciona bien"