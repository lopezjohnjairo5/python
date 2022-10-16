"""
Generador de Sudokus
====================

generador de sudokus con posibilidad de 
exportar como libro pdf 
"""
from tkinter import *
import random as rd
import pyautogui
import time
import threading as td

class Sudoku:
    """
        class Sudoku:
        :parameters: none
    """
    def __init__(self):
        """
            method __init__:
            :parameters: none
        """
        self.sudoku_full = []
        self.sudoku_game = []
        
    def window(self):
        """
        metodo window, no recibe parametros,
        encargado de retornar una ventana Tk
        """
        wind = Tk()
        wind.title("sudoku")
        wind.geometry("1100x600+10+10")
        return wind
    
    def interface(self):
        """
        metodo interface, no recibe parametros,
        encargado de poner los elementos de la 
        interface
        """
        #obj
        w = self.window()
        
        #labels
        self.var_label = StringVar()
        self.var_label.set("DIFICULTAD")
        lbl = Label(w,textvariable=self.var_label).place(x=25,y=5)
        
        #vars
        posx = 25
        posy = 25
        rows = 0
        cols = 0
        #inputs -> generando la cuadricula
        #game
        for i in range(1,82):
            exec(f"self.var_{str(rows)}_{str(cols)} = StringVar()")
            exec(f"entry_{str(rows)}_{str(cols)} = Entry(w,textvariable=self.var_{str(rows)}_{str(cols)},font='Helvetica 18 bold',justify='c').place(x={posx},y={posy},width=40,height=40)")
            print(f"entry_{str(rows)}_{str(cols)}\n")
            posx += 50
            cols += 1 #utilizado para nombrar las variables y entrys
            
            if(i%3 == 0):
                posx += 10
            
            if(i%9 == 0):
                posy += 50
                rows += 1
                if(rows%3 == 0):
                    posy += 10
                posx = 25
                cols = 0
        
        
        #vars
        posx = 600
        posy = 25
        rows = 0
        cols = 0
        
        #game solution
        for i in range(1,82):
            exec(f"self.sol_var_{str(rows)}_{str(cols)} = StringVar()")
            exec(f"self.sol_entry_{str(rows)}_{str(cols)} = Entry(w,textvariable=self.sol_var_{str(rows)}_{str(cols)},font='Helvetica 18 bold',justify='c')")
            exec(f"self.sol_entry_{str(rows)}_{str(cols)}.place(x={posx},y={posy},width=40,height=40)")
            print(f"self.sol_entry_{str(rows)}_{str(cols)}\n")
            posx += 50
            cols += 1 #utilizado para nombrar las variables y entrys
            
            if(i%3 == 0):
                posx += 10
            
            if(i%9 == 0):
                posy += 50
                rows += 1
                if(rows%3 == 0):
                    posy += 10
                posx = 600
                cols = 0
        
        #entry name
        self.var_nombre =StringVar()
        self.var_nombre.set(1)
        entry_name = Entry(w,textvariable=self.var_nombre).place(x=25,y=550,width=100,height=20)
        
        #dificultad
        self.n_opcion = IntVar() #solo se usa una variable para el conjunto de radio btns
        self.n_opcion.set(1) #asigando un valor por defecto
        
        radio_btn_1 = Radiobutton(w,text="muy facil",variable=self.n_opcion, value=1).place(x=25,y=510) 
        radio_btn_1 = Radiobutton(w,text="facil",variable=self.n_opcion, value=2).place(x=125,y=510) 
        radio_btn_2 = Radiobutton(w,text="medio",variable=self.n_opcion, value=3).place(x=225,y=510) 
        radio_btn_3 = Radiobutton(w,text="dificil",variable=self.n_opcion, value=4).place(x=325,y=510) 
        
        
        #btns
        btn1 = Button(w,text="generar",width=7,command=lambda : self.include_sudoku()).place(x=405,y=510)
        btn2 = Button(w,text="capturar",width=7,command=lambda : self.screen_record_save(self.var_nombre.get())).place(x=500,y=510)
        #btn3 = Button(w,text="coordena",width=7,command=lambda : self.coordenadas_ventana(w)).place(x=600,y=510)
        
        w.mainloop()
        
    def coordenadas_ventana(self,w):
        """
        metodo coordenadas_ventana (no utilizado), metodo encargado
        de capturar y mostrar las coordenas actuales de la ventana
        """
        win_posx = w.winfo_width()
        win_posy = w.winfo_height()
        x=w.winfo_pointerx()
        y=w.winfo_pointery()
        print(f"tamanno : {win_posx}:{win_posy}")
        print(f"puntero: {x}:{y}")
        
    def include_sudoku(self):
        """
        metodo include_sudoku encargado de llenar las casillas del sudoku
        """
        self.main() #ejecutamos main para que se cree todo el sudoku y se almacene en las variables del init
        
        #llenamos el sudoku completo-lado izq
        for i in range(0,9):
            for j in range(0,9):
                exec(f"self.var_{str(i)}_{str(j)}.set(self.sudoku_full[i][j])")
        

        self.sudoku_game = self.ocult_matriz(self.n_opcion.get(),self.sudoku_full)  #pasamos la dificultad y el sudoku lleno  
        
        #actualizamos el label de la dificultad segun el radio button
        if(self.n_opcion.get() == 1):
            self.var_label.set("Dificultad: Muy fácil")
        
        elif(self.n_opcion.get() == 2):
            self.var_label.set("Dificultad: Fácil")
        
        elif(self.n_opcion.get() == 3):
            self.var_label.set("Dificultad: Medio")
        
        elif(self.n_opcion.get() == 4):
            self.var_label.set("Dificultad: dificil")
        
        #llenamos el sudoku para juego con huecos -- lado derecho
        for i in range(0,9):
            for j in range(0,9):
                exec(f"self.sol_var_{str(i)}_{str(j)}.set(self.sudoku_game[i][j])") 
                if(self.sudoku_game[i][j] != ""):
                    exec(f"self.sol_entry_{str(i)}_{str(j)}.configure(state='disabled')")      
                else:        
                    exec(f"self.sol_entry_{str(i)}_{str(j)}.configure(state='normal')")                
        
        
    
    def first_array(self):
        """
        crea array aleatorio de numeros 
        entre el 1 y el 9
        """
        nums = []
        while len(nums)<9:
            num = rd.randint(1,9)
            if (num not in nums):
                nums.append(num)
            
        return nums


    def matriz_full(self,s,array):
        """
        llena la matriz basandose 
        en un array
        """
        arr=[]
        
        for i in range(s,len(array)):
            arr.append(array[i])
            
        for j in range(0,s):
            arr.append(array[j])
        
        return arr


    def ocult_matriz(self,dif,mat):
        """
        reemplaza algunos de los valores
        por *.
        """
        cant=0
        conj=[]
        self.mat = mat
        
        if(dif==1):
            #muy facil
            cant=20
        elif(dif==2):
            #facil
            cant=40
        elif(dif==3):
            #medio
            cant=60
        elif(dif==4):
            #dificil
            cant=80
            
        while(len(conj)<cant):
            conj.append([rd.randint(0,8),rd.randint(0,8)])
        
        for i in conj:
            self.mat[i[0]][i[1]]=""
            
        return self.mat


    def change_columns(self,matr):
        """
        intercambia columnas de la matriz principal
        """
        n_mat = matr
        pos = [[rd.randint(0,2),rd.randint(0,2)],
        [rd.randint(3,5),rd.randint(3,5)],
        [rd.randint(6,8),rd.randint(6,8)]]
        
        for x in pos:
            for i in range(0,len(n_mat)):
                var_pass = n_mat[i][x[0]]
                n_mat[i][x[0]] = n_mat[i][x[1]]
                n_mat[i][x[1]] = var_pass
        
        return n_mat
        
        
    def change_rows(self,matr):
        """
        intercambia columnas de la matriz principal
        """
        n_mat = matr
        pos = [[rd.randint(0,2),rd.randint(0,2)],
        [rd.randint(3,5),rd.randint(3,5)],
        [rd.randint(6,8),rd.randint(6,8)]]
        
        for x in pos:
            for i in range(0,len(n_mat)):
                var_pass = n_mat[x[0]][i]
                n_mat[x[0]][i] = n_mat[x[1]][i]
                n_mat[x[1]][i] = var_pass
        
        return n_mat
                
        
    def main(self):
        """
        metodo encargado de llamar a las funciones/metodos
        encargados de crear el sudoku full
        """
        #creando matriz respuesta
        matriz=[]


        f1 = self.first_array()
        matriz.append(f1)
        for i in range(1,9):
            if(i%3==0):
                exec(f"f{i+1} = self.matriz_full(1,f{i})")
            else:
                exec(f"f{i+1} = self.matriz_full(3,f{i})")
            exec(f"matriz.append(f{i+1})")

        print("\nmatriz original\n")
        for i in matriz:
            print(i)

        #mezclando matriz
        print("\nmezclando filas y columnas\n")
        self.sudoku_full=self.change_columns(matriz)
        self.sudoku_full=self.change_rows(self.sudoku_full)
        

    def screen_record_save(self,suf="1"):
        """
        metodo encargado de capturar la pantalla y almacenarlo en la pc
        """
        #capturando la pantalla
        capture = pyautogui.screenshot(region=(25,40,1070,510))
        
        #guardando la imagen
        capture.save(f"capture_{suf}.png")

s = Sudoku()
s.interface()   
     
#s.main()        