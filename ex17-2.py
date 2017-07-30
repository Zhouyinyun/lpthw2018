# -*- coding: utf-8 -*-
from sys import argv #在sys软件中载入argv特性。
from os.path import exists #同过import调用exists命令。

script, from_file, to_file = argv #把打开脚本时输入的文件名放入变量filename中

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()