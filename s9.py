name=input("enter a string:")
non_repeated={}
for ch in name:
    if ch not in non_repeated:
        non_repeated[ch]=1
    else:
        non_repeated[ch]+=1
for key,value in non_repeated.items():
    if value==1:
        print(key)
        break
