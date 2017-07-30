# -*- coding: utf-8 -*-
from sys import argv #从系统中提取参数

script, one, two, three, fourth = argv

print "The script is called:", script
script = raw_input("what is script?")
print "Your first variable is:", one
print "Your second variable is:", two
print "Your third variable is:", three
print "Your fourth variable is:", fourth

