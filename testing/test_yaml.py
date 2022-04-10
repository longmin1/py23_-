"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import yaml


# pip install pyyaml


def test_yaml():
    # safe_load: 把yaml 格式 转成python对象
    # safe_dump: 把python对象 转成yaml格式
    with open("./datas.yml", encoding="utf-8") as f:
        result = yaml.safe_load(f)

        add_P0_datas = result.get("add").get("P1_2").get('datas')
        add_P0_ids = result.get("add").get("P1_2").get('ids')

        print(f"P0 级别的datas {add_P0_datas}")
        print(f"P0 级别的ids {add_P0_ids}")
