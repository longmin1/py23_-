"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import logging
from time import sleep

import allure

"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# 测试模块
import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas(level):
    # safe_load: 把yaml 格式 转成python对象
    # safe_dump: 把python对象 转成yaml格式
    with open("./datas.yml", encoding="utf-8") as f:
        result = yaml.safe_load(f)

        add_datas = result.get("add").get(level).get('datas')
        add_ids = result.get("add").get(level).get('ids')

        print(f"{level} 级别的datas {add_datas}")
        print(f"{level} 级别的ids {add_ids}")
    # P0 级别的datas [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]]
    # P0 级别的ids ['2个整数', '2个浮点数', '整数+浮点数']
    return [add_datas, add_ids]


# 大的功能点
@allure.feature("计算器功能")
class TestCalculator:
    add_P0_datas = get_datas("P0")[0]
    add_P0_ids = get_datas("P0")[1]
    add_P1_1_datas = get_datas("P1_1")[0]
    add_P1_1_ids = get_datas("P1_1")[1]
    add_P1_2_datas = get_datas("P1_2")[0]
    add_P1_2_ids = get_datas("P1_2")[1]
    add_P2_datas = get_datas("P2")[0]
    add_P2_ids = get_datas("P2")[1]

    # 冒烟测试用例
    @pytest.mark.run(order=3)
    @pytest.mark.P0
    # 需要至少两个参数，第一参数是字符串- 里面存放要传递的参数，以逗号隔开
    # 第二参数，就是我们要传递的数据序列（可以列表，可以元组），每个序列里存放一组数据
    @pytest.mark.parametrize('a,b, expect',
                             add_P0_datas,
                             ids=add_P0_ids)
    @allure.story("相加功能--有步骤")
    def test_add0(self, a, b, get_calc, expect):
        # sleep(1)
        logging.info(f"参数：{a}，{b}，期望结果：{expect}")
        # 测试相加方法
        with allure.step("相加操作"):
            result = get_calc.add(a, b)
        logging.info(f"结果：{result}")
        # 实际结果 对比 预期结果
        with allure.step("结果验证"):
            assert result == expect

    # 有效边界值
    @pytest.mark.run(order=1)
    @pytest.mark.P1_1
    @pytest.mark.parametrize('a,b, expect',
                             add_P1_1_datas,
                             ids=add_P1_1_ids)
    @allure.story("相加功能")
    def test_add1(self, get_calc, a, b, expect):
        sleep(1)

        result = get_calc.add(a, b)
        allure.attach.file("./image/logo.jpg", name="截图", attachment_type=allure.attachment_type.JPG, extension=".jpg")
        assert result == expect

    # 异常情况处理
    @pytest.mark.run(order=2)
    @pytest.mark.P1_2
    @pytest.mark.parametrize('a,b, errortype',
                             add_P1_2_datas,
                             ids=add_P1_2_ids)
    @allure.story("相加功能")
    def test_add3(self, get_calc, a, b, errortype):
        # pytest 封装的一种处理异常的方式
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.add(a, b)

        print(e.typename)

    @pytest.mark.run(order=-1)
    @pytest.mark.P2
    @pytest.mark.parametrize('a,b, errortype',
                             add_P2_datas,
                             ids=add_P2_ids)
    @allure.story("相加功能")
    def test_add4(self, get_calc, a, b, errortype):
        # pytest 封装的一种处理异常的方式
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.add(a, b)

        print(e.typename)

    @allure.story("相除功能")
    def test_div(self, get_calc):
        print("相除功能")
        result = get_calc.div(1, 1)
        assert result == 1
