from main import *

def test_process_operation():
    for a in range(0, 100):
        for b in range(0, 100):
            assert process_operation(a, "+", b) == a+b
            if (b != 0):
                assert process_operation(a, "/", b) == a/b
            else:
                assert process_operation(a, "/", b) == Error.DIV_ZERO
            assert process_operation(a, "*", b) == a*b
            assert process_operation(a, "-", b) == a-b
    assert process_operation(a, "g", b) == Error.UNS_OP
    assert process_operation("a", "*", "b") == Error.UNS_VAL

def test_unmix():
    assert unmix("10-2") == [[10, 2], ["-"]]
    assert unmix("3-") == Error.BAD_EQ
    assert unmix("/5") == Error.BAD_EQ
    assert unmix("g-2") == Error.UNS_VAL
    assert unmix("3") == [[3], []]

def test_operate():
    assert operate(unmix("2+3")) == 5
    assert operate(unmix("7/0")) == Error.DIV_ZERO
    assert operate(unmix("10+2/4-4*6")) == -13.5
