name=input("enter a string:")
count1=0
count2=0
for s in name:
    if s.isalpha():
        if s.isupper():
            count1+=1
        else:
            count2+=1
print(f"the number of uppercase characters are {count1}")
print(f"the number of lowercase characters are {count2}")
    
