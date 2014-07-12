#coding=utf-8

import androidhelper
from os.path import exists
from os import makedirs
from os import access
import os

droid = androidhelper.Android()

'''
*name:class_data.py
*author:equationl
*date:2014.06.23
*公共类集合
'''

'''
*初始化类
*Public_init
     ||
setpath()  setfiledata()
check_path()  check_file()
'''
class Public_init:
   def __init__(s):
      s.path = ''
      s.filedata = []
    
   #设置路径
   def setpath(s,path):
      s.path = path
      
   #设置文件数据
   def setfiledata(s,filedata):
      s.filedata = filedata
      
   '''*检测路径是否存在，不存在则创建。
      *成功不返回，失败返回失败信息'''
   def check_path(s):
      if not exists(s.path):
         try:
            makedirs(s.path)
         except Exception as e:
            return e
    
   '''
      *校验文件。
      *存在则返回 True ,不存在则尝试创建
      *filedata为元组，形如:
         filedata(file_name,file_hex_data) 
            file_name为文件相对路径
            file_hex_data为文件十六进制数据
      *创建成功不返回，失败返回错误信息。
   '''        
   def check_file(s):
       if access(s.path+s.filedata[0],os.F_OK):
          return True
       else:
          try:
             f = open(s.path+s.filedata[0],'w')
             f.write(s.filedata[1].decode('hex'))
             f.close()
          except Exception as e:
             return e

      
