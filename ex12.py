# -*- coding: utf-8 -*-
age = raw_input("How old are you? ") #显示提示你多大了，用户输入之后，赋值给age
height = raw_input("How tall are you? ")#同上。
weight = raw_input("How much do you weigh? ")#同上。

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight) #最后给出上面的答案，一起打印出来。双引号内。你给什么内容，就显示什么内容。
