# Ecrivez votre code ici !
num1=input("donner le premier nombre : ")
num2=input("donner la 2 eme nombre : ")
listop=["+","-","*","/"]
op=input("choisit loperation que vous voulez")
# tester les inputs ! 
if not num1.isnumeric() or not  num1.isnumeric() or not  op in listop :
    raise SystemExit("Fin du programme")
else :
 # num1 et num2 ---> entier 
 num1=int(num1)
 num2=int(num2)
 match op :
    case "+" : 
     resultat=num1+num2
     print(f"{num1}+{num2}={resultat}")
    case "-" :
      resultat=num1-num2
      print(f"{num1}-{num2}={resultat}")
    case "*" :
      resultat=num1*num2
      print(f"{num1}*{num2}={resultat}")
    case "/" :
      if num2==0 :
        print("tu peux pas diviser par zero !!")
      else  :
       resultat=round(num1/num2,2)
       print(f"{num1}/{num2}={resultat}")  
    case _ :
     print("votre operation doit appartient a ["+","-","*","/"]")   

