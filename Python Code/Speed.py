dist = input("Give me a distance in KM: ")
time = input("Give me a time in Hour: ")

dist = float(dist)
time = float(time)

speed = (dist/1000)/(time/3600)
print("Median speed: "  + str(speed) + " m/s")
