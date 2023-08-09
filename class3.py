import threading
import time

def abc():
    
    l = [1,2,3,4,5]
    ans=[]
    
    for i in l:
        ans.append(i**3)
    time.sleep(1)
    print(ans)



t1=threading.Thread(target=abc,args=( ))

t1.start()
t1.join()
