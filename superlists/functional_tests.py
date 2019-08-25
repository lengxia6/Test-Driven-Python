#-*- coding:utf-8 -*-
#Autor:Ziting

from selenium import webdriver
import unittest
import time

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):

        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get("http://localhost:8000")
        # # self.assertIn('To-Do',self.browser.title)
        # header_text = self.browser.find_element_by_tag_name('h1').text
        # # self.assertIn('To-Do',header_text)



        # 应用邀请输入一个待办事项



        inputbox = self.browser.find_element_by_id('id_new_item')
        # 输入框输入"购买孔雀毛"
        inputbox.send_keys('购买孔雀羽毛')

        # 按回车键后，待办表格中显示 "购买孔雀毛"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: 购买孔雀羽毛')


        self.fail('Finish the test')



if __name__ == '__main__':
    unittest.main(warnings='ignore')







