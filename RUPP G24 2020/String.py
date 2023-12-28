

from asyncore import loop


st=input("input string:")
for i in st:
    print(i,end='')
sized=len(st)
for i in range(0,sized):
    print(st[i],end='')

print("")
print("UPPER CASE:",str.upper(st))
print("Lower case:",str.lower(st))
print("String:",st)

# if
# loop
# function
# araay
# class