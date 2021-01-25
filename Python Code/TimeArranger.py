seconds = input("Give me a time in Seconds: ")
seconds = float(seconds)

hours = int(seconds/3600)
minutes = int((seconds - (int(hours)*3600))/60)
seconds = int(seconds - ((int(hours)*3600) + (int(minutes)*60))

print(hours)
print(minutes)
print(seconds)