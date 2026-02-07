# Écrivez votre code ici !
from bs4 import BeautifulSoup
with open("index.html",'r') as file :
    soup=BeautifulSoup(file , 'html.parser')

# extraire les donnnes 

title=soup.title.string
pagertitle=soup.find(id="titre")
productname=soup.find_all('h2')
productprice=soup.select("p.price")
productdescription=soup.find_all("p")

#declarer les dicitinnaires 

product1=dict()
product2=dict()
product3=dict()

# creer les fonction d'optimisation 

def newdescription():
     liste=[]
     for i in range(len(productdescription)) :
          if "Description" in productdescription[i].string :
               liste.append(productdescription[i].string)
     return liste


liste=newdescription()

driniprodcut=[product1,product2,product3]

# modifier les prix 

def  modifprice():
 for j in range(3) :
   otherliste=productprice[j].string.split()
   otherliste.remove('Prix:')
   numbre=""
   nega="".join(otherliste)
   for i in range(2) :
      numbre+=nega[i]
   numbre=1.2*int(numbre) 
   numbre=str(numbre)+'$'
   productprice[j].string=numbre
modifprice()

#remplire les donnes dans les dictionnaires

def remplirlesdict(product , j) :
     product["name"]=productname[j].string
     product["price"]=productprice[j].string
     product["Description"]=liste[j].string
     return product 

#affecter  les produits

product1=remplirlesdict(product1 , 0)
product2=remplirlesdict(product2 , 1)
product3=remplirlesdict(product3 , 2)
 
# afficher les donnes 

print(product1)
print(product2)
print(product3)

