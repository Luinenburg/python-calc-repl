from main import *

def test_process_operation():
    for a in range(0, 100):
        for b in range(0, 100):
            assert process_operation(a, "+", b) == a+b
            if (b != 0):
                assert process_operation(a, "/", b) == a/b
            else:
                assert process_operation(a, "/", b) == None
            assert process_operation(a, "*", b) == a*b
            assert process_operation(a, "-", b) == a-b
    assert process_operation(a, "g", b) == None

def test_unmix():
    assert unmix("10-2") == [[10, 2], ["-"]]
    assert unmix("3-") == None
    assert unmix("/5") == None
    assert unmix("g-2") == None
    assert unmix("3") == [[3], []]

def test_operate():
    assert operate(None) == None
    assert operate(unmix("7/0")) == None
    assert operate(unmix("10+2/4-4*6")) == -13.5
