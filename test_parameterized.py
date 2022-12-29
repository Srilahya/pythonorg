import pytest

@pytest.mark.parameterize("a,b,c",["lahya","sri","sree"],["la","hya","sr"])
def test_functionAdd(a,b,c):
    assert a+b == c


#
import pytest

@pytest.mark.parameterize("a,b,c",[(1,2,3),(7,8,9)]
def test_functionAdd(a,b,c):
    assert a+b == c

#
import pytest

@pytest.mark.parameterize("a,b,c",[(1,2,2),(7,8,9)]
def test_functionMultiply(a,b,c):
    assert a*b == c

#
@pytest.mark.parameterize("a,b,c",[(6,3,2),(7,8,9)]
def test_functionDivide(a,b,c):
    assert a/b == c


#
@pytest.mark.parameterize("a,b,c",[(4,2,2),(7,8,9)])
def test_functionSub(a,b,c):
    assert a-b == c