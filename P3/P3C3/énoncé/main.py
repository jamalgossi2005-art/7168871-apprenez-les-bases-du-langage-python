# Écrivez votre code ici !

import csv 
liste1=[]
liste2=[]
en_tete=["nom","heures_travaillees"]
def    read():
        with open("input.csv", "r") as file_r :
         reader=csv.DictReader(file_r )
         for line in reader :
          liste1.append(line['nom'])
          liste2.append(str(float(line['heures_travaillees'])*15))
          
def   write():
           
        with open("output.csv" , "w") as file_w :
         writer=csv.writer(file_w , delimiter=',')
         writer.writerow(en_tete) 
         for nom , heure in zip (liste1,liste2) :
               liste=[nom,heure]
               writer.writerow(liste)
        
read()

write()
# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
