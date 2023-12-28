#Sum = 2+4+8+16+...+n

n = int(input("Enter n: "))
i=1
while(i<=n):
    print("Sum",pow(2,i))
    i =i+1
    
#Primary number using Function

def checkPrime(x):
    for i in range(2, x):
        if n%i==0:
            return 1

print("Enter a Number: ", end="")
n = int(input())

p = checkPrime(n)
if p==1:
    print("\n" +str(n)+ " is not a Prime Number")
else:
    print("\n" +str(n)+ " is a Prime Number")

#Input Output of array

lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) 
print("Array:",lst)

#Create class product(id, name, qty, price)
from re import I
from socket import INADDR_ALLHOSTS_GROUP


class product:
    def init(self, id,name, qty, price):
        self.id = id
        self.name = name
        self.qty = qty
        self.price = price
    def display(self):
        print(self.id,"\t",self.name,"\t",self.qty,"\t",self.price)
id = int(input("Enter id: "))
name = input("Enter name: ")
qty = input("Enter qty: ")
price = int(input("Enter price: "))
p = product(id,name,qty,price)
p.display()