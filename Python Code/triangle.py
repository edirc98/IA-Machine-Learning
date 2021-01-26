h = int(input("Give a high for the triangle: "))
c = "-"
cT = ""
i = 0

while i < h*2:
    if i < h:
        cT += c
    else:
        cT = cT[:-1]

    i += 1
    print(cT)
