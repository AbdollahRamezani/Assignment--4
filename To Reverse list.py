n=int(input("please insert number fo list: "))
list1=[]
list2=[]
for i in range(n):
    num=int(input("please enter number: "))
    list1.append(num)
    i+=1
i=n-1
while i>=0 :
    list2.append(list1[i])
    i-=1
print(list1)    
print(list2)    

