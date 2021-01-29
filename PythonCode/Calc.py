# 被测类：计算器
class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        #捕获分母为零
        if b==0:
            return "分母不为零"

        return a / b