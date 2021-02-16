from random import randint
from time import sleep

heads=0
tails=0
print("Assingment_2 M.Tech CS")
print("Sample space={Heads, Tails}")
flip=int(input("how many times, you want to toss the coin:"))

for i in range(flip):
    result=randint(0,1)
    sleep(1)
    if result==0:
         print("Heads")
         heads+=1
    else:
        print("Tails")
        tails+=1
k=heads/flip
l=tails/flip
print("The results are :")
print("prob. of Heads:",k)
print("prob. of Tails:",l)
