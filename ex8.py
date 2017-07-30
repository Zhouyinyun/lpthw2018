# -*- coding: utf-8 -*-
formatter = "%s %r %r %r" #变量命名，四个格式化字符，而且都是原始数据。打印出来的回事括号内的原始数据。


print formatter % (1, 2, 3, 4) #打印1，2，3，4
print formatter % ("你好", "two", "three", "four") #打印 “one”,这样，带上双引号。
print formatter % (True, False, False, True) #打印正确、错误、错误、正确。没有双引号。
print formatter % (formatter, formatter, formatter, formatter) #打印 “%r %r %r %r” 这样四次。
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) # 打印四句。带上双引号。不带后面的逗号。
