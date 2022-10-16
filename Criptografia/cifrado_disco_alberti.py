"""
difrado Alberti
"""

def sort_values_table(external_letter, internal_letter, table):
    """
    funcion encargada de reordenar los valores de la tabla
    para que las letras seleccionadas queden en la posicion inicial,
    con esto simulamos el giro del disco interior y su coincidencia con el 
    exterior
    """
    #cortamos de cero hasta la letra introducida por el usuario para dejarla de primera (en cada 'lista/disco')
    #luego pegamos la parte cortada al final de la misma lista
    internal_text = table[1][table[1].index(internal_letter):] +table[1][:table[1].index(internal_letter)]
    external_text = table[0][table[0].index(external_letter):] +table[0][:table[0].index(external_letter)]

    new_table = [external_text,internal_text]
    #external_text = "".join(external_text[:external_text.index(external_letter)] + external_text[external_text.index(external_letter):])
    
    #print("External letter: {0}\nInternal letter: {1}".format(external_text,internal_text))
    
    return new_table
    

def encrypting_text(ext_letter,text,table):
    """
    funcion encargada de cifrar el texto claro introducido
    por el usuario, teniendo presente la tabla pasada por 
    parametro
    """
    #ponemos de primera la letra mayuscula del disco exterior que usaremos como referencia para decodificar
    ciphertext = ext_letter
    
    for i in text:
        #buscamos cada letra a encriptar en el disco externo (lista mayusculas)
        if(i.upper() in table[0]):
            #obtenemos la posicion de la letra en el disco exterior y la usamos
            #para localizar la letra que le corresponde en el otro disco
            #finalmente la concatenamos
            ciphertext += table[1][table[0].index(i.upper())]
    
    return ciphertext

if(__name__ == '__main__'):

    #variables
    not_allowed_external = ["h","j","k","u","y","w"," "]
    not_allowed_internal = ["h","j","u"," "]

    #tabla utilizada para simular los discos concentricos de Alberti
    table = [
            [chr(c).upper() for c in range(97,123) if (chr(c) not in not_allowed_external)],
            list(set(chr(c) for c in range(97,123) if (chr(c) not in not_allowed_internal)))
            ]

    #añadimos & a la segunda lista
    table[1].append("&")        

    #añadimos los numeros del 1 al 4 a la primera lista
    for i in range(1,5):
        table[0].append(str(i))

    #imprimir
    print("\nDISCO DE ALBERTI\n")
    for i in table:
        print("{0}".format(i))
         
    #capturamos los valores necesarios
    agreed_letter = ""
    external_letter = ""

    #nos aseguramos que se introduzcan valores permitidos (solo los que estan en las listas de la tabla)
    while external_letter.upper() not in table[0]:
        external_letter = input("\nletra disco exterior: ").upper()
    
    while agreed_letter.lower() not in table[1]:  
        agreed_letter = input("letra acordada (disco interior): ") #letra acordada del disco interno    
    
    #capturando el texto a encriptar
    plain_text = input("Introduzca el texto a encriptar: ").upper()

    #moviendo/reordenando valores de las tablas
    n_table = sort_values_table(external_letter, agreed_letter, table)
    
    #llamado a funcion encargada de la encriptacion
    final_text = encrypting_text(external_letter,plain_text,n_table)
    
    print("\n\nTabla final:\n{0}\n{1}\n\nTexto en claro: {2}\nTexto cifrado: {3}".format(n_table[0],n_table[1],plain_text,final_text))