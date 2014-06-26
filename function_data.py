#coding=utf-8

import androidhelper
from config import *  #载入程序配置、常量信息
from filedata import * #载入资源文件数据

droid = androidhelper.Android()

'''
*name:function_data.py
*author:equationl
*date:2014.06.23
*公共函数集合
'''

'''
*首次启动运行函数
*启动该程序时应先启动该函数
'''
def public_install():
   #创建一个 Public_init 实例
   install = Public_init()
   
   #校验文件夹是否存在
   for i in PATHDATA:
      install.setpath(i) #设置路径
      install.check_path() #检测并创建路径
      
   #校验资源文件
   for i in FILEDATA:
      install.setpath(ROOTPATH) #设置根目录
      install.setfiledata(i) #设置文件数据
      install.check_file() #检测并创建文件
      