from time import sleep
import yaml
from .base import Base



class MainPage(Base):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def click_address(self,tip,path):
        from .address_page import AddressPage
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        with open(path, 'r')as f:
            cookies = yaml.safe_load(f)
            # print(cookies)
        for cookie in cookies:
            if 'expiry' in cookie.keys():  # expiry里面有浮点数非法参数，所以可以删除
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(3)
        self.find(tip).click()
        return AddressPage(self.driver)




