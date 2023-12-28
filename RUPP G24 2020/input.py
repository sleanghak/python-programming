

# print("Enter the Number of Days: ")
# num = int(input())

# year = int(num/365)
# week = int((num%365)/7)
# days = int((num%365)%7)

# print("Total Number of Year(s): ")
# print(year)
# print("Total Number of Week(s):")
# print(week)
# print("Total Number of Day(s):")
# print(days)

day =int(input("Input Day:"))
year=day //365
day=day%365
week=day //7
day=day%7
print("Year=",year)
print("Week=",week)
print("Day=",day)