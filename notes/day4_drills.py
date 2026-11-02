for n in range (1, 15):     #variable n in range (loop), from 1 to 15
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

print("Hello World, next line please \n")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #list of numbers from 1 to 10    
for n in list:
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

reversed_list = list[::-1] #reversing the list
print(reversed_list)