# -*- coding:UTF-8 -*-
from sys import argv #导入模块sys

script, filename = argv #解包。

txt = open(filename) #命令行，打开解包后的文件。

print "Here's your file %r:" % filename #打印这句话，告诉用户，这是你的文件。
print txt.read() #这时显示文件内容。

print "Type the filename again:"#打印双引号里的内容
file_again = raw_input("> ") #再次输入你的文件。提示是>，

txt_again = open(file_again) #再次打开文件。

print txt_again.read() #再次显示内容。

