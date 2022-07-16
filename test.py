chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
word = "BZEEZ"
word2 = "SZEEZ"


def repeating_letters(x):
    global y
    count = {}
    for s in x:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    thislist = []
    for key in count:
        if count[key] > 1:
            thislist.append(key)
            thislist.append(count[key])
    return thislist


repeating_letters(word)
place1 = ''.join(str(x) for x in repeating_letters(word))
print(place1[2:4])
place2 = ''.join(str(x) for x in repeating_letters(word2))
print(place2[0:2])
if place2 == place1:
    print("OK")
else:
    print("not OK")

tvojstring = "bbb"
mojstring = "A%s%sAA" % (tvojstring[0],"%s")
mojstring = mojstring % ("c"+tvojstring)
print("A{}AA".format("A"))

print(mojstring)
mojstring = "%s%s%s"
print("%s"*4)

z = "%s"
while z in mojstring:
    mojstring = mojstring % ("%d")
print(mojstring)