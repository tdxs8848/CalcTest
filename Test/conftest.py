
import pytest

from PythonCode.Calc import Calculator


@pytest.fixture(scope="class")
def calc():
    print("计算器测试开始......")
    calc = Calculator()
    yield calc

# @pytest.fixture(scope="function")
# def calc():
#     print("\n计算开始......")
    # calc = Calculator()
    # yield calc
@pytest.fixture(scope="function",autouse="true")
def myfixture(request):
    print("\n计算测试开始")


    #teardown
    def fin():
        print("结束计算...")
    request.addfinalizer(fin)