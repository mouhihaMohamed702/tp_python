Number = int(input("Entrer un nomber positive : "))
    
print("les nomber divise par 3 et non par 5 :")
for i in range(1, Number+1):
    if i % 3 == 0 and not i % 5 == 0:
        print(i)
