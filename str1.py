s1=input("enter a string:")
s2=""
for i in range(-1,(-len(s1)-1),-1):
    s2+=s1[i]
if s1==s2:
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")

    
