name = input("Enter a string: ")
result = ""
for ch in name:
    if ch != " ":
        result += ch
print(result)
