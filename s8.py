name =input("enter a string:")
new_string=""
for ch in name:
    if ch in new_string:
        continue
    new_string+=ch
print(new_string)
        
