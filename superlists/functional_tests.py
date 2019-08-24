#-*- coding:utf-8 -*-
#Autor:Ziting

from selenium import webdriver
import unittest
import time


# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert  'Django ' in browser.title
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):

        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get("http://localhost:8000")
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # 应用邀请输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # 输入框输入"购买孔雀毛"
        inputbox.send_keys('购买孔雀毛')

        # 按回车键后，待办表格中显示 "购买孔雀毛"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text =='1: 购买孔雀毛' for row in rows)
        )

        self.fail('Finish the test')








if __name__ == '__main__':
    unittest.main(warnings='ignore')







