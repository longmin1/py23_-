"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# conftest.py 文件中的函数是不需要导入的
# 位置：项目根目录
# 查找路径：
# 1. 先从当前模块找->再从当前目录->再往上级节点查找
import time

import pytest

from pythoncode.calculator import Calculator


@pytest.fixture()
def login():
    print("根目录的 login")


@pytest.fixture()
def conndb():
    print("根目录的 conndb")


@pytest.fixture(scope="class")
def get_calc():
    calc = Calculator()
    yield calc
    print("结束测试")


@pytest.fixture(scope='function',autouse=True)
def calcu_fix():
    print("开始计算")
    yield
    print("结束计算")


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = 'output/log/' + now + '.logs'
    # request是 pytest中内置的fixture
    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(log_name)
