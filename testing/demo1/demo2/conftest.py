"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest


@pytest.fixture
def login():
    print("xiaoming --> login")


@pytest.fixture
def conndb():
    print("xiaoming --> login")
