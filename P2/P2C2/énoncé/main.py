liste=[]
listevalider=[]
add=True
print("ajouter une note")
while add :
    liste.append(int(input("entrer une note")))
    if not input("est ce que tu veux ajouter une note ? ")=='oui' :
      add=False
somme=0
for x in liste :
   somme+=x
   if x>=10 :
      listevalider.append(int(x))
for x in range(len(listevalider)) :
 if x==0 :
  print(f" somme    moyenne     les notes valider ")
  print(f" {somme}        {round(somme/2,3)}            {listevalider[x]} ")
 else :
  print(f"                            {listevalider[x]}    ")# Ecrivez votre code ici !
