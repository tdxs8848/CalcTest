# 被测类：计算器
class Calculator:
    def add(self, a, b):
        if type(a)!=int and type(a)!=float and type(b)!=int and type(b)!=float:
            return "输入类型错误"
        return a + b

    def div(self, a, b):
        #捕获分母为零
        if b==0:
            return "分母不为零"
        if type(a)!=int and type(a)!=float and type(b)!=int and type(b)!=float:
            return "输入类型错误"
        return round(a/b,2)
