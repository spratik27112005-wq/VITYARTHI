import time
import sys

def is_chronic(n):
    a=1
    total=0
    for i in range(n):        
        num=a*i
        if num==n:
            total=1
        a+=1
        i+=1
    return total

n1=int(input("Enter the number to be checked: "))
start_time = time.time()
re=is_chronic(n1)
if re==1:
    print("It is a chronic number")
else:
    print("It is not a chronic number")

end_time = time.time()
time_taken = end_time-start_time
print("time taken:",time_taken,"seconds")
print("memory utilised:",sys.getsizeof(is_chronic))
