# -*- coding: utf-8 -*-
x = "There are %d types of people." % 10 #这里有十种不同的人。
binary = "binary" #二进制
do_not = "don't" #缩写
y = "Those who know %s and those who %s." % (binary, do_not) #那些知道二进制，那些不知道二进制。

print x #打印 这里有十种不同的人。
print y #打印 那些知道二进制，那些不知道二进制

print "I said: '%r'." % x #我说：‘这里有十种不同的人。’
print "I also said: '%s'." % y #我也说：‘那些知道二进制，那些不知道二进制。’

hilarious = False #滑稽是错误的。
joke_evaluation = "Isn't that joke so funny?! %r" #那个笑话好笑吗？不好。

print joke_evaluation % hilarious #打印

w = "This is the lefe side of..." 
e = "a string with a right side."

print w + e

a = "hello, "
b = "world "
c = "!"

print a + b + c
