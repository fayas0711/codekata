low,upp=raw_input().split()
low=int(low)
upp=int(upp)
for num in range(low+1,upp):
    order=len(str(num))
    sum=0
    temp=num
    while temp > 0:
        degit = temp % 10
        sum+=degit ** order
        temp //= 10
    
    if num == sum:
        print(num)
