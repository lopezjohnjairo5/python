"""
ejercicio contador de digitos
cuenta la cantidad de digitos/numeros
presentes en una cadena ingresada
"""
def cont_numbers_1():
    txt = input("Introduzca un texto alfanumerico: ")
    cont = 0
    for t in txt:
        if(t.isdigit()):
            cont += 1
            
    print("la cantidad de numeros en la cadena es: {0}".format(cont))
    
    
def cont_numbers_2(): 
    txt = input("Introduzca un texto alfanumerico: ")
    print(len(list(filter(lambda x: x.isdigit(),list(txt)) )))
    
    
#cont_numbers_2()    

def cont_numbers_2():
    """
    contar cantidad de valores numericos
    mediante expresiones regulares
    """
    pass