name=input("enter a sentence:")
reversed_sentence=""
for i in range(len(name),1,-1):
    reversed_sentence+=name[i]
print(reversed_sentence)
