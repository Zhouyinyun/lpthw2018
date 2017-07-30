# -*- coding: utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers): #定义函数
    print "You have %d chesses!" % cheese_count 
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:" #直接给函数传递数字
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:" #给它变量
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:" #给它数学表达式，计算出来之后，再运行函数
cheese_and_crackers(10 + 20, 5 + 6)

# print combine
print "And we can combine the two, variables and math:" #还可以把数学表达式和变量合起来用
# give the function numbers.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
