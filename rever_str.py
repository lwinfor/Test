import os

def test(arr,n=0):
    if n == len(arr):
        return ""
    return test(arr,n+1)+arr[n]

def test1():
    arr = "abcdefg"
    ans = test(arr)
    print(ans)

def test2():
    dp =[ [False]*5  for _ in range(5) ]
    print(dp)

def test3():
    def gcd(a,b):
        return a if b==0 else gcd(b,a%b)
    print(gcd(12,5))
    print(gcd(21,28))
    print(gcd(28,21))


for item in range(5,1,-1):
    print(item)

print(123//10)

a=[1,2,3]
a.pop()
print(a)

a.pop(0)
print(a)

print(ord('a')-ord('A'))
a=chr(ord('b') + 1)
print(a)


print(1<<0)