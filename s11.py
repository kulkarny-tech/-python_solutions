name=input("enter a string:")
duplicates={}
for ch in name:
    if ch  in duplicates:
        duplicates[ch]+=1
    else:
        duplicates[ch]=1
for key,value in duplicates.items():
    if value>1:
        print(key)
        
        
        
        
    
        
