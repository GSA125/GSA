# This program print "Hello!" 10 times.

value=True
while(value):
    print("Tell me 2 numbers and i will tell you the square of every number between those")
    first=input()
    second=input()
    for square in range(int(first),int(second)+1):
        print(square**2)
