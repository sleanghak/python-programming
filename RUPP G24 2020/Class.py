

class Kid:
    def __int__(self,id,n,age):
        self.id=id
        self.name=name
        self.age=age

    def display(self):
        print(self.id,"\t",self.name,"\t",self.age)

id=int(input("id:"))
name=input("name:")
age=int(input("age:"))
k=Kid(id,name,age)
k.display()