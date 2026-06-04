name =input("enter the string:")
s=input("enter a character:")
count=0
for char in name:
    if char==s:
        count+=1
print(f"the occurance of the character is{count}times")
