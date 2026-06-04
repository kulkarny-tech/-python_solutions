name=input("enter a string:")
char_count={}
for s in name:
    if s in char_count:
        char_count[s]+=1
    else:
        char_count[s]=1
print(char_count)
