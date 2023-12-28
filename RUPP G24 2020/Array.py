

# num = [20,40,60,80,30]

# s=0

# for i in num:
#     s=s+i
# print("sum=",s)

#-------------------<<*>>----------------------

num=[]
n=int(input("Input n: "))
for i in range(0,n):
    print("input num: ",i+1,end='')
    x=int(input())
    num.append(x)
for i in num:
    print(i,end='')