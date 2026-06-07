name=input("enter a string:")
removed_spaces=""
for ch in name:
    if ch==" ":
        removed_spaces+="*"
    else:
        removed_spaces+=ch
print(removed_spaces)
