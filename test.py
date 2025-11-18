import random
print("welcom to gues the number!")
print("can you guess what it is?")
print("(0 - 100)")
x=int(input())
if x < 100:
    print("too hight")
if x > 100:
    print("too low")