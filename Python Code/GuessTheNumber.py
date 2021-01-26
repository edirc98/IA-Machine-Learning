from random import randint
print("A number between 0 and 10 will be generated, guess it!")

guessed = False
lower_times = 0
higher_times = 0
total_times = 0
value = randint(0, 10)
while guessed != True:
    number = input("Guess the number: ")
    if number.isdigit():
        if int(number) < value:
            print("Too LOW")
            total_times+=1
            lower_times+=1
        elif int(number) > value:
            print("Too HIGH")
            total_times+=1
            higher_times+=1
        elif int(number) == value:
            print("CORRECT, You guess it!!")
            total_times+=1
            guessed = True
    else:
        print("Invalid input") 
        total_times+=1
        

print("Total tries: " + str(total_times))
print("Total higher: " + str(higher_times))
print("Total lower: " + str(lower_times))