# Print Multiplication Table if No. is divisible by 3 & 5.

# print(9%3)
a = 15;
# print(a % 3 & a % 5)

if (a % 3 & a % 5): 
    for i in range(1,11):
        z = a*i 
        print(z)
else:
    print("number is not divisible by 3 or 5") 


