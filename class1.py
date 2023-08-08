def abc():
    for i in range(1,11):
        yield i

for i in abc():
    print(i)
