from random import choice

# The code below is broken:
# jenna = ["awesome", "cool", "amazing", "the best person ever", "hot asf", "smart asf", "going to the best university ever", "the nicest person ever"]
# justin = ["weird", "odd", "cringy", "irrelevant", "low iq", "annoying", "living on the wost coast", "going to apply to berkeley"]

# Here is the fixed version:
jenna = ['annoying', 'cringe', 'weird and sleeps on the floor', 'is basically a turtle', 'is broke', 'pays $20K a year on dorms', 'needs to drink more water']
jusin = ['amazing', 'big IQ', 'sleeps in a bed unlike jenna', 'is built different', 'will fold jenna in half', 'is GOATED', 'knows who joe is']

name = input("jenna or justin?")
if name == "jenna":
    print(name, "is", choice(jenna))
elif name == "justin":
    print(name, "is", choice(justin))
else:
    print("joe mama")
