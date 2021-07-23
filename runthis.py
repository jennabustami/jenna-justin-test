from random import choice
#run to see facts
jenna= ["awesome", "cool", "amazing", "the best person ever", "hot asf", "smart asf", "going to the best university ever", "the nicest person ever"]
justin= ["weird", "odd", "cringy", "irrelevant", "low iq", "annoying", "living on the wost coast", "going to apply to berkeley"]

name = input("jenna or justin?")
if name== "jenna":
    print( name, "is", choice(jenna))
elif name == "justin":
    print(name, "is", choice(justin))
else:
    print("joe mama")

