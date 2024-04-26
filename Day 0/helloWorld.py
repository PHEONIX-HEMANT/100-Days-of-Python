print("Hello World")        # print function takes an valid object as argument.
print("Jai Hind", "My India")

#multiline comment
'''
This is a 
multiline 
comment
'''
#Escape Sequences
print("Hey\nThere")
print("Please \"Do Not\" Execute")

#More on print statement
# print(object(s), sep=seperator, end=end, file=file, flush=flush)
# seperator tells how to seperate the objects, default sep = space
# end tells what to print at the end, default end = new line
# file : an object with a write method
print("Hey",6,7)
print("Hey",6,7,sep='~')
print("Hey",6,7,sep='~', end="OOO")
print("Hemant")

import sys

sampleFile = open('output.txt', 'w')
print("I","Love","My","",sep='~', end="Country", file=sampleFile)