from faker import Faker
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from time import sleep

from mine_web_shizhan_change.page.base import Base


class AddressPage(Base):


    def random_data(self):
        fake=Faker(locale="zh_CN")
        self.name=fake.name()
        self.accid=fake.ssn()
        self.mobile=fake.phone_number()

    def add_member(self):
        self.random_data()
        ele_located=(By.CSS_SELECTOR,'.qui_btn.ww_btn.js_add_member')
        self.finds(ele_located)[1].click()
        self.find((By.CSS_SELECTOR, '#username')).send_keys(self.name)
        ele = self.find((By.CSS_SELECTOR, '#memberAdd_acctid'))
        ele.send_keys(self.accid)
        self.find((By.CSS_SELECTOR, '#memberAdd_phone')).send_keys(self.mobile)
        self.action.scroll_from_element(ele, 0, 500).perform()
        self.find((By.CSS_SELECTOR, '.js_btn_save')).click()
        return self.name

    def get_member(self):
        a=self.add_member()
        print(a,type(a))
        def func(x):

            eles=self.finds((By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)'))#两种方式一样的  都是获取名字的列表所有值
            for ele in eles:
                if ele.get_attribute('title')==a:
                    return ele.get_attribute('title')
            sleep(2)
            self.finds((By.CSS_SELECTOR,'.ww_pageNav_info .js_next_page'))[0].click()

        a_new=self.wait_by_fun(func)
        print(a_new)
        assert a_new==a

    def add_department(self):
        '''添加部门'''
        self.find((By.CSS_SELECTOR,'.member_colLeft_top_addBtnWrap.js_create_dropdown')).click()
        self.find((By.CSS_SELECTOR, '.js_create_party')).click()
        self.find((By.CSS_SELECTOR, '.inputDlg_item > input')).send_keys('搬砖部门')
        self.find((By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list')).click()
        self.finds((By.CSS_SELECTOR, '.jstree-anchor'))[1].click()
        self.find((By.XPATH,'//a[@d_ck ="submit"]')).click()
        self.wait_ele_visibilit((By.CSS_SELECTOR,'#js_tips'))
        return self.find((By.CSS_SELECTOR,'#js_tips')).text








# AddressPage().add_member()