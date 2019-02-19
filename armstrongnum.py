h=int(raw_input())
sum = 0
temp = h
while temp > 0:
    degit = temp % 10
    sum += degit ** 3
    temp //= 10
if h == sum:
    print("yes")
else:
    print("no")
