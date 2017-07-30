from sys import argv

script, filename = argv

target = open (filename,'w')

print "Now i'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

you = "her"

print "I'm going to write these to the file, \"is that ok with %r  " % you

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n\"")
target.write(line3)
target.write("\n")
target.write(line1+"\n"+line2+"\n"+line3+"\n")

print "And finally, we close it."
target.close()

