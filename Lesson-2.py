x = 15
y = 10
s = "Odessa"
d = "Milch, Brod, Obst"
m = [1, 2, 3, "4", 5]

if x < y:
    print("Olga")
    if "Odessa" == s:
        print("Ukraine")
        if "Brod" in d:
            print("Germany")
elif x > y:
    print("Kuzlo")
    if "4" not in m:
        print("Herno")
    elif 1 in m:
        print("Moskow")
else:
    print("Valik")
