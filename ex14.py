# -*- coding: utf-8 -*-
from sys import argv #这是导入sys模块。

script, user_name, her_name = argv #然后解包
prompt = "！！！"

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like her %s?" % her_name
likes = raw_input(prompt)

print "Where do you live with %s?" % her_name
lives = raw_input("where ")

print "What kind of computer do you have?"
computer = raw_input("What ")

print "can you do %r ?" % her_name

print """
Alright, so you said %r about liking her.
You live in %r with her. Not sure where it is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
