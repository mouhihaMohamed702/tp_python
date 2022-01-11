
mot = input("entrer le mot : ")
print("la premier lettre est : {0}, et la dernier lettre est : {1}".format(mot[0], mot[-1]))
print("The mot entre le deuxieme  et le quatrieme charactere est : {0}".format(mot[1:3]))
print("le mot inverse est : {0}".format(mot[::-1]))
print("les lettres paire dans le mot: {0}".format(mot[::2]))

mot2 = input("Entrer la 2 eme mot qui conteint plusieur espaces : ")
print("le mot est: " + mot2)
print("le mot sans espace est: " + mot2.replace(" ", "").upper())
