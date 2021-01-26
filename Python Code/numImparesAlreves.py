i = 100
total = 0
while i > 0:
    if i%2 != 0:
        total = total + i
        print(i)
    i-=1
print(total)