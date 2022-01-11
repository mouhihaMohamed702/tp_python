    Number = int(input("Entrer un nomber entier : "))
    Binary_Number = bin(Number)

    if Binary_Number[-1] == '0':
        print("{0} est un nomber paire".format(Number))
    else:
        print("{0} est un nomber impaire".format(Number))
