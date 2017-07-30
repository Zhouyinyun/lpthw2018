from sys import argv

script, filename = argv

txt = open(filename)
print txt.read()

print "choose your filename"