import calendar

def leap():
    for i in range(2001,2030):
        if(i%4==0):
            yield i 


for i in leap():
    print(i)
