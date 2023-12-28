# print("===========================")
# print("1. Riels to Dollar ")
# print("2. Dollars to Riels ")
# print("===========================")
# while True:
#     ch=input("input choise: ")
#     if ch=='1':

#         riels=float(input("input riels: "))
#         rate=float(input("input rate: "))
#         dollar=riels/rate
#         print(riels)
#         print(rate)
#         print("Riels to dollars ","{:.2f}".format(dollar),"$")
        
#     elif ch=='2':

#         Dollar=float(input("input dollar: "))
#         Rate=float(input("input rate: "))
#         Riel=Dollar*Rate
#         print(Dollar)
#         print(Rate)
#         print("Dollars to Riels: ","{:.2f}".format(Riel)," Riels")

#     else:
#         break




l=[]
n=int(input("Input number of provinces: "))
for i in range (0,n):
   name=input("Input Name of Provinces: ")
   num=int(input("Input Number of People :"))
   s=[num,name]
   l.append(s)
   l.sort()
print(l)