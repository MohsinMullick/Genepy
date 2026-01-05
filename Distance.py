def dist(values):
    return max(values) - min(values)
print(dist([5, 2, 9, -3, 7]))  # Output: 12

#reverse
num=int(input("Enter 3 digit: "))
a=num%10
print(a)
b=(num//10)%10
print(b)
c=(num//100)
print(c)
reverse=a*100+b*10+c
print(reverse)