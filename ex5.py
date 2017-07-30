# -*- coding: utf-8 -*-
name = 'Zed A. Shaw' #他叫zed
age = 35 # not a lie # 35岁
height = 74 # inches 这里是round(755.3)
transfer_height = 2.54 * height # cm
weight = 180 # lbs
transfer_weight = 0.45359237 * weight #kg
eyes = 'Blue' #为什么这里要在单引号里？文字都在单引号里，数字直接写出。
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall, %d cm." % (height, transfer_height)
print "He's %d pounds heavy, %d kg." % (weight, transfer_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
