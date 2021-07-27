from random import choice
# run to see facts
jenna = ["annoying", "okay", "jenna", "mid", "smart but not as smart as justin", "going to an okay school", "the meanest person ever"]
justin = ["interesting", "fun", "funny", "important", "high iq", "living on the best coast", "going to apply to berkeley (in jennas dreams)"]

name = input("jenna or justin? ")
if name == "jenna":
    print(name, "is", choice(jenna))
elif name == "justin":
    print(name, "is", choice(justin))
else:
    print("joe mama")
