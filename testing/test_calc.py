"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# 测试模块
from pythoncode.calculator import Calculator


class TestCalculator:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_add0(self):
        # 测试相加方法
        calc = Calculator()
        result = calc.add(1, 1)
        print(result)
        # 实际结果 对比 预期结果
        assert result == 2
