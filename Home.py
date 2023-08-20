s = input("Vvedite stroku  ")
if s.isalpha() and s.islower():
    print(s.upper())
elif s.isdigit():
    print(int(s))
else:
    print("Stroka smeshannaya")






