cases= [" "," "," "," "," "," "," "," "," "]
tour=0
symbole=" "
victoire=0
joueur1=0
caseChoisie= 0

print(cases[0],cases[1],cases[2])
print(cases[3],cases[4],cases[5])
print(cases[6],cases[7],cases[8])
while tour!=9 and victoire==0:
    if joueur1==0:
        symbole="x"
    else:
        symbole="o"
    caseChoisie= int(input("Quelle case remplir: "))
    cases[caseChoisie]=symbole
    print(cases[0],cases[1],cases[2])
    print(cases[3],cases[4],cases[5])
    print(cases[6],cases[7],cases[8])
    for i in range(3):
        if cases[i]==symbole and cases[i+1]==symbole and cases[i+2]==symbole:
            victoire=1
    for j in range(3):
        if cases[j]==symbole and cases[j+3]==symbole and cases[i+6]==symbole:
            victoire=1
    if cases[0]==symbole and cases[4]==symbole and cases[8]==symbole:
            victoire=1
    if cases[2]==symbole and cases[4]==symbole and cases[6]==symbole:
            victoire=1

    if joueur1==0:
        joueur1=1
    else:
        joueur1=0

if tour==9:
    print("La grille est complète")
else print("Vous avez gagné")

    

    
    





