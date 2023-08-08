import time

def abc():
    for i in range(1,11):
        if(i%2==0):
            yield i

def xyz():
    for i in range(1,11):
        if(i%2==1):
            yield i

print("Even Number : ")            
for i in abc():
    time.sleep(0.3)
    print(i)

print("Odd Number : ")
for i in xyz():
    time.sleep(0.3)
    print(i)

