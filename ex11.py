# -*- coding: utf-8 -*-
print "How old are you?", #打印双引号里的内容。
x = raw_input(float()) #输入 raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    x, height, weight)#最后打印上面输入的全部内容。
