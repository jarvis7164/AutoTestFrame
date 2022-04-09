# -*- coding: utf-8 -*-
# @Time    : 2022/3/27 13:17
# @Author  : Jarvis
# @Email   : jiamiao12@qq.com
# @File    : jd.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


page_url = 'https://www.jd.com'

elements = [
    {'name': 'search_ipt', 'desc': '搜索框点击', 'by': (By.ID, u'key'), 'ec': 'presence_of_element_located', 'action': 'send_keys()'},
    {'name': 'search_btn', 'desc': '搜索按钮点击', 'by': (By.CLASS_NAME, u'button'), 'ec': 'presence_of_element_located', 'action': 'click()'},
]
