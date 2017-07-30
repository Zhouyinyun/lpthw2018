# -*- coding: utf-8 -*-
cars = 100 #汽车100辆
space_in_a_car = 4.0 #每辆车四个位置
drivers = 30 #司机三十个人。
passengers = 90 #乘客一共90人。
cars_not_driven = cars - drivers #没有使用的汽车等于汽车总数减去司机数量。
cars_driven = drivers #已经开走的汽车，当然等于那些已开走的汽车上的司机数。
carpool_capacity = cars_driven * space_in_a_car #载运辆等于已开的汽车乘于每辆车的座位数
average_passengers_per_car = passengers / cars_driven #每辆车的平均乘客等于乘客总数除以投入使用的汽车。


print "There are", cars, "cars available." #有100辆可以使用的汽车。
print "There are only", drivers, "drivers available." #但是只有30个司机
print "There will be", cars_not_driven, "empty cars today."  #所以有70辆车不能投入使用。
print "We can transport", carpool_capacity,"people today."  #我们可以运载120位乘客
print "We have",passengers,"to carpool today." #我们今天需要运送90位乘客。
print "We need to put about",average_passengers_per_car,"in each car." #我们需要让每辆车坐上三个人。
