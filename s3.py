name=input("enter a string").lower()
vowels=0
consonants=0
for s in name:
    if s.isalpha():
        if s in "aeiou":
            vowels=vowels+1
        else:
            consonants=consonants+1
print(f"There are{vowels}vowelspresent in the string")
print(f"There are{consonants}consonants present in the string")
