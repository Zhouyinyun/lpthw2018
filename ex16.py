# -*- coding: utf-8 -*-
from sys import argv #导入模块，或者说，启动一个软件。

script, filename = argv 

print "We're going to erase %r." % filename #打印
print "If you don't want that, hit CTRL-C (^C)." #如果不要 提示^C.
print "If you do want that, hit RETURN." #如果想要这样，就按回车。

raw_input("?") 

print "Opening the file..." #打开
target = open(filename, 'w') #把文件打开，W？

print "Truncating the file. Goodbye!" #打印清空文件的命令，再见。
target.truncate() 

print "Now I'm going to ask you for three lines." #打印

line1 = raw_input("line 1: ") #第一行？用户输入。读取了，再书写
line2 = raw_input("line 2: ") #第二行？
line3 = raw_input("line 3: ") #第三行？

print "I'm going to write these to the file." #打印

target.write(line1) #目标书写第一行。
target.write("\n") #目标书写换行符，之后，依次第二行，换行，第三行，换行。
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it." #打印我们要关闭它啦。
target.close() #关闭。
