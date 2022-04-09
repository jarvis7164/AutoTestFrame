# -*- coding: utf-8 -*-
# @Time    : 2022/3/27 12:25
# @Author  : Jarvis
# @Email   : jiamiao12@qq.com
# @File    : data.py
# @Software: PyCharm
import pandas as pd


# def excel_read(file, **kwargs):
#     data_dict = []
#     try:
#         data = pd.read_excel(file, **kwargs)
#         print(data)
#         data_dict = data.to_dict('records')
#     finally:
#         return data_dict
#
# IO = 'test_jd_desktop.xls'
# test = excel_read(IO)
# print(test)

def excel_read(file):
    data_dict = []
    try:
        IO = file
        data = pd.read_excel(io = IO)
        data_dict = data.to_dict('records')
    finally:
        return data_dict

# data = excel_read("test_jd_desktop.xls")
# print(data)