from app.main import add

def test_add():
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-2, -3) == -5 
    assert add(1, 4) == 5
    assert add(5, 3) == 8
    assert add(3,5)==8