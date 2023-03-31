'''
# Write a program to sum of all natural no. from given from 1 to n.

print("Enter the Natural no. you want to sum of : ")
n = int(input())

for i in range(1, n):
    n = n+i
    
print(n)
'''

# Insertion Sort

a = [5,4,10,1,6,2]
n = 6

for i in range(1,n):
    temp = a[i]
    j = i-1
    
    while(j >= 0 & a[j] > temp):
        a[j + 1] = a[j]
        j = j-1
    a[j+1] = temp
    
print("End of the program")