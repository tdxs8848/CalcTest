
import sys

import pytest
import yaml

sys.path.append('..')
print(sys.path)
from PythonCode.Calc import Calculator

def get_datas(dataName):
    with open("./datas/calc.yml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return (datas[dataName]['datas'], datas[dataName]['ids'])


# def get_add_datas():
#     with open("./datas/calc.yml",encoding='utf-8') as f:
#         datas = yaml.safe_load(f)
#     return (datas['add']['datas'], datas['add']['ids'])


# yaml json excel csv xml
# 测试类
class TestCalc:
    add_datas: list = get_datas('add')
    div_datas: list = get_datas('div')

    # 前置条件
    def setup_class(self):
        print("计算器测试开始......")
        self.calc = Calculator()


    def setup(self):
        print("\n开始计算...")

    def teardown(self):
        print("结束计算...")

    #后置条件
    def teardown_class(self):
        print("计算器测试结束......")

    @pytest.mark.parametrize("a, b, result", add_datas[0], ids=add_datas[1])
    def test_add(self, a, b, result):
        print(f"a={a} , b ={b} ,result={result}")
        assert result == self.calc.add(a, b)

    # def test_add1(self):
    #     datas = [[1, 1, 2], [100, 400, 300], [1, 0, 1]]
    #     for data in datas:
    #         print(data)
    #         assert data[2] == self.calc.add(data[0], data[1])

    # done: 完善相加功能
    # done: 相除功能
    @pytest.mark.parametrize("a, b, result", div_datas[0], ids=div_datas[1])
    def test_div(self,a,b,result):
        print(f"a={a} , b ={b} ,result={result}")
        assert result == self.calc.div(a, b)