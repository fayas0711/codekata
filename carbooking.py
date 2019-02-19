print("welcome to XcarX")
places=["tambaram","adayar","ambathur"]
dist=[35,30,50]
print("where u want to go")
print("1.tambaram,2.adyar,3.ambathur")
choice=int(input())
if choice==1:
    kms=dist[0]
elif choice==2:
    kms=dist[1]
else:
    kms=dist[2]
print(" availabe cars are nano, micro, nano, prime")
print("what type of car u want?")
car=int(input())
carname=["nano","micro","mini","prime"]
nano=2
micro=4
mini=6
prime=8
if car==1:
    price=kms*nano
elif car==2:
    price=kms*micro
elif car==3:
    price=kms*mini
else:
    price=kms*prime
print("the estimated price is", price) 
print("your selected place is",places[choice-1])
print("your selected car is",carname[car-1])

status=["confirmed","not confirmed"]
bchoice=int(input())
if bchoice==1:
    print("your booking is",status[bchoice-1])
else:
    print("not confirmed",status[bchoice-1])
