# -*- coding: utf-8 -*-
# Here's some new strange stuff, remember type it exactly.这里有一些新奇的东西，一字不差地打印出来。

days = "Mon Tue Wed Thu Fri Sat Sun" #日子就是周一到周日
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #月份就是一月到八月，而且，每一个都换行。

print "Here are the days: ", days #打印双引号里的内容。周一到周日。不带引号。
print "Here are the months: ", months #打印双引号里的内容。并且分行显示。

print """
There's something going on here.
With the threee double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""# 打印三双引号里的内容。
print "we are talking about %r ?" % months #打印双引号里的内容，并且显示格式化字符原始数据。带上双引号。最后，会显示单引号。
print "we are talking about %s ?" % months #打印双引号里的内容，并且分行显示。
