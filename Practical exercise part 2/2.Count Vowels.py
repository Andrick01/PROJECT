a=input("Enter a string:")
b=0
c='aeiou'
for i in a:
    if i in c:
        b+=1
print("No of Vowels:",b)