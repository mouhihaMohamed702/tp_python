l=[]
s=0
nbrNote=0
note=float(input("entrer une novelle note positive"))
min=note
max=note
while note>=0:
    l.append(note)
    nbrNote=nbrNote+1
    s=s+note
    if note<min:min=note
    if note>max:max=note
    print(" la moyenne est",s/nbrNote)
    print("la note la plus base est",min)
    print("la meilleure note est", max)
    note = float(input("entrer une novelle note positive"))
