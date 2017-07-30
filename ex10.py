# -*- coding: utf-8 -*-
tabby_cat = "\tI'm tabbed in." #命名变量 /t就是tab的意思，缩进。
persian_cat = "I'm split\non a line."#在on这个位置换行。NEWline
backslash_cat = "I'm \\ a \\ cat."#在a前面留一个反斜杠，cat前面也留一个。

fat_cat = """
I'll do a list:
\t* cat food
\t2 Fishies
\t3 Catnip\n\t4 Grass
"""# 在这里面随便玩。缩进，另外在最后一行，4之前换行，换行之后再缩进。

print tabby_cat #打印双引号里的内容
print persian_cat #打印双引号里的内容
print backslash_cat #打印双引号里的内容
print fat_cat #打印三引号里的内容。
        
A = "A\nB\n\t*C"
print '%s' % A


print "%r" % "\"\",A\n\tB"
print '%s' % "\"\",A\n\tB"


        
