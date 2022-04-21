"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import allure
import pytest


@allure.feature("aaaa")
class TestDemo:

    @allure.story("a1")
    def test_demo1(self):
        print()


    @allure.story("a2")
    def test_demo2(self):
        print()
