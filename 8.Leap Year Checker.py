a=int(input("Enter year:"))
if((a%100!=0 or a%4==0) or a%400==0):
    print(a,"is leap year")
else:
    print(a,"is not a leap year")