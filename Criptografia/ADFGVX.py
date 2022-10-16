"""
cifrado ADFGVX
"""
#creando matriz aleatoria
def create_matriz():
    matriz = [[' ','A','D','F','G','V','X'],[],[],[],[],[],[]]
    conjunto = set(chr(a) for a in range(97,123)) #se usa el conjunto para que queden en desorden los valores
    for i in range(0,10):
        conjunto.add(str(i))

    conjunto = list(conjunto) #se convierte en lista para poder trabajarlo
    j = 1

    # añadimos los valores del conjunto a la matriz (6 valores por cada fila)
    for i in range(0,len(conjunto)):
        matriz[j].append(conjunto[i])
        if((i+1) % 6 == 0):
            j += 1
            
    #insertamos las letras mayusculas de las filas
    for i in range(1,len(matriz)):
        matriz[i].insert(0,matriz[0][i])

    #imprimimos la matriz
    for i in matriz:    
        print(i)
    
    return matriz


def new_text():
    """
    funcion encargada de capturar un nuevo texto 
    y de eliminar los espacios
    """
    
    text = input("\nIntroduzca el texto a encriptar: ").lower()
    new_text = ""
    #removemos los espacios encontrados
    for i in text:
        if (i != " "):
            new_text += i

    return new_text


    
def first_text(mat, value):
    letters = ""
    #recorremos la matriz y vamos comparando con cada letra ingresada
    for i in range(1,7):
        for j in range(1,7):
            if(mat[i][j] == value):
                #print(mat[i][j])
                letters += mat[i][0] + mat[0][j] 
                # retornamos la fila y la columna, representadas con las letras mayusculas
                return letters



def search_text_values(txt,mat):
    """
    funcion encargada de 
    buscar cada letra ingresada por
    el usuario en la tabla.
    """
    pos_text = ""
    
    #recorremos el texto completo, letra a letra    
    for l in txt:
        #buscamos la posicion de cada letra y la concatenamos en la variable pos_text
        pos_text += first_text(mat, l)

    print("Texto encriptado inicial: {0}".format(pos_text))
    return pos_text


def key_word(k):
    """
    funcion encargada de capturar una palabra clave y asociarla
    con el valor encriptado.
    """
    k_word = input("Introduzca una palabra clave: ").upper()
    len_word = len(k_word) 
    k_word += k
    matriz = []
    min = 0
    max = 0
    
    #creando matriz a partir del texto concatenado
    for i in range(0,len(k_word)+1):
        if( i > 0 and i % len_word == 0 or i == len(k_word)):
            min = max
            max = i
            matriz += [list(k_word[min:max])]
            
    return matriz



def sort_table(table):
    """
    funcion encargada de ordenar la 
    tabla pasada por parametro segun 
    el valor del encabezado y creamos 
    la frase cifrada final
    """
    index_item = 0
    ordered_list = sorted(table[0])
    final_text = ""
    
    print("\nResultado de ordenar la tabla: \n{0}".format(ordered_list))
    
    #recorremos los encabezados previamente ordenados
    for i in ordered_list:
        #obtenermos el indice de cada elemento en la tabla desordenada
        index_item = table[0].index(i)
        
        #recorremos cada fila buscando en la posicion indicada
        for r in range(1,len(table)):
            try:
                final_text += table[r][index_item]
            except:
                pass
    
    return final_text


if(__name__ == '__main__'):
    new_matriz = create_matriz()
    k = search_text_values(new_text(),new_matriz)
    table = key_word(k)
    for i in table:
        print(i)
    print("\nTexto encriptado final: {0}".format(sort_table(table)))