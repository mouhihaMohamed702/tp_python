
import random

n = random.randint(0, 10)
mess = "?"
for i in range(0,3):
    var = input("Entrez un nombre")
    var = int(var)
    if var < n:
        mess = "trop bas"
        print(var, mess)

    else:
        mess = "trop haut"
        print(var, mess)
    if var == n:
        mess = "bravo !"
        print(var, mess)
        break

