name =input("enter a string:")
seen=set()
for ch in name:
    if ch in seen:
        print(ch)
        break
    else:
        seen.add(ch)
