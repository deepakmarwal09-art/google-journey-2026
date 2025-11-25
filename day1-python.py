#fibonacci code
n = int(input())
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b

#Reverse a number
n = int(input())
rev = int(str(n)[::-1])
print(rev)

#Print table
n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

