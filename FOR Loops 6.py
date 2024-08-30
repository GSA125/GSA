# This program print "Hello!" 10 times.

user_num=int(input())
if user_num > 1:
    for i in range(2,user_num):
        if(user_num/i)==0:
            print("thats is not a prime number")
            break
    else:
        print("thats a prime number")
else:
    print("is not a prime number")

print("           ")
print("           ")
print("           ")
print("           ")
print("           ")
   
    
