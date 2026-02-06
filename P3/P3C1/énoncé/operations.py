# la somme 
def somme(num1 , num2):
    return num1+num2
#le produit
def produit(num1 , num2):
    return num1*num2
#la division
def division(num1 , num2):
    try:
     return num1/num2
    except ZeroDivisionError:
       print("impossible de diviser par zero ")
#la soustraction      
def soustraction(num1 , num2) :
     return num1-num2

