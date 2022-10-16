"""
encriptacion mediante 
atbash y cifra cesar
"""

#atbash
def atbash(txt_claro):
    """
    definimos 2 veces el alfabeto, el primero en orden y 
    el segundo invertido
    """
    alph_1 = [chr(i) for i in range(97,123)]
    alph_2 = [chr(i) for i in range(122,96,-1)]
    
    #definimos 2 variables para trabajar 
    texto_claro = txt_claro
    texto_encriptado = ""

    #recorremos letra a letra el texto introducido por el usuario
    for i in range(0,len(texto_claro)):
    
        #verificamos que la letra se encuentre en el alfabeto
        if(texto_claro[i] in alph_1):
            
            # concatenamos a la variable de texto_encriptado 
            # la nueva letra obtenida del segundo alfabeto y
            # basada en la posicion de la letra original
            # en el alfabeto inicial
            
            texto_encriptado += texto_encriptado.join(
            alph_2[alph_1.index(texto_claro[i])])
       
    #retornamos el texto encriptado    
    return texto_encriptado    

#capturamos el texto introducido por el usuario
texto_claro = input("\nTexto a encriptar: ")

#mostramos el texto introducido y el resultado del proceso de cifrado
print("El texto en claro es: {0}".format(texto_claro))        
print("El texto atbash es: {0}".format(atbash(texto_claro)))        