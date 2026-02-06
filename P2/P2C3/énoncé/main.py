def salaire_mensuel(slaire_A) :
    return slaire_A/12
def salaire_hebdomadaire(salire_M) :
    return salire_M/4 
def salaire_horaire(salaire_H , nbreH) :
      return salaire_H/nbreH
salire_anneul=int(input("donner votre salaire annuel : "))
#HT=nombres des hueres
HT=int(input("donner le nombre des heures que vous travaillez dans chaque semaine"))
print(f"votre salaire horaire est : {round(salaire_horaire(salaire_hebdomadaire(salaire_mensuel(salire_anneul)),HT))} ")
