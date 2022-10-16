"""
programa encargado de insertar 
contenido de un txt a una bd
"""
import pymysql as pm


def read_txt(txt):
    """
    encargado de leer el documento de texto a enviar a la bd
    """
    new_list = []
    
    with open(txt,mode="r") as f:
        for l in f.readlines():
            #new_list.append(l.split(" : ")[0]) #poner este al leer el archivo de departamentos_y_capitales_colombia
            new_list.append(l.split(" : "))

    #print(new_list) #poner este al leer el archivo de departamentos_y_capitales_colombia
    return new_list


def connect_to_bd():
    conn = pm.connect(host="localhost",db="ubicacion_db",passwd="",user="root")
    cursor = conn.cursor()
    
    return [cursor,conn]
    
    
def search_into_table(c,table,field,value):
    """
    busca valores en la tabla pasada por parametro
    """
    #print("SELECT * FROM '{0}' WHERE '{1}' = {2}".format(table,field,value))
    try:
        cursor = c.execute("SELECT * FROM '{0}' WHERE '{1}' = '{2}';".format(table,field,value))
        result = cursor.fechall() 
    except:
        return False
    else:
        return True



def search_id_from_table(c,r_field,table,field,value):
    """
    busca y retorna el valor id 
    de la tabla 
    pasada por parametro
    """
    #print("SELECT {0} FROM {1} WHERE {2} = '{3}';".format(r_field,table,field,value))
    sql = "SELECT {0} FROM {1} WHERE {2} = '{3}';".format(r_field,table,field,value)
    c.execute(sql)
    result = c.fetchone() 
    return result


def insert_into_table(c,table,fields,values):
    """
    insertar valores en la tabla
    """
    sql = "INSERT INTO {0} ({1}) VALUES ('{2}');".format(table,fields,values)
    try:
        c[0].execute(sql)
    except Exception as e:
        print("error al insertar en la bd: {0}".format(e))
    
    c[1].commit()
    
    
def insert_into_table_where(c,table,field1,field2,value1,value2):
    """
    insertar valores en la tabla
    """
    sql = "INSERT INTO {0} ({1},{2}) VALUES ('{3}','{4}');".format(table,field1,field2,value1,value2)
    try:
        c[0].execute(sql)
    except Exception as e:
        print("error al insertar en la bd: {0}".format(e))
    
    c[1].commit()    
    
    
if(__name__ == "__main__"):
    """
    #buscando e insertando los departamentos
    txt = read_txt("departamentos_y_capitales_colombia.txt")
    
    c = connect_to_bd()
    for v in txt:
        if not(search_into_table(c[0],"departments","Department",v)): #revisar sql de la funcion
            insert_into_table(c,"departments","Department",str(v))
            
    """        
    
    #buscando e insertando los municipios teniendo presente los departamentos ya insertados
    txt = read_txt("departamentos_ciudades.txt")
    c = connect_to_bd()
    n_v = []
    for v in txt:
        n_v = (v)[0].split(":")
        print(n_v[0].lstrip() +","+n_v[1].lstrip())
        result = search_id_from_table(c[0],"idDepartment","departments","Department",n_v[0])
        print(str(result[0]))
        insert_into_table_where(c,"cities","City","idDepartment",str(n_v[1].lstrip()),result[0])
        #if not(search_into_table(c[0],"departments","Department",v)):
        #    insert_into_table(c,"departments","Department",str(v))
        #    