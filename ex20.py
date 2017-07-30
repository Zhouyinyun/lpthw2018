# -*- coding: utf-8 -*-
from sys import argv #在sys中载入argv特性

script, input_file = argv #解包，在打开脚本时输入的文件名放入变量input_file中。

def print_all(f): #函数定义参数
    print f.read() #读取f文档

def rewind(f): #
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
