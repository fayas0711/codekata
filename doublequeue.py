print("Queue")
print("the available functions are given below:")
print(" enqueue or dequeue or size or emptiness or exit")
a=input()
a=int(a)
l=[50,21]
b=len(l)
print("enter the num")
if a==1:
    print("you have selected Enqueue function")
    s=input()
    s=int(s)
    cha=input()
    if s==0:
        l.insert(0,cha)
    else:
        l.append(cha)
    print("your inserted value is" ,l)
if a==2:
    print("you have selected Dequeue function")
    d=input()
    d=int(d)
    if d==1:
        l.pop(0)
    elif d==2:
        l.pop()
    print("your current value is ",l)
if a==3:
    print("you have selected size function")
    print("the length is",len(l))
if a==4:
    print("you have selected emptiness function")
    if b==0:
        print("it is empty")
    else:
        print("the number of values are",b)
if a==5:
    print("exit")
if a==6:
    print("select from above options")
