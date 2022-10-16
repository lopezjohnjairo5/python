#!/usr/bin/env python3
"""
probado en linux 100% funcional
"""
import subprocess
import time
import os
import random as rd

class Fondo_pantalla:
	def __init__(self):
		self.ciclo = True
		self.orden = ""
		self.ind = 0
		self.ruta = "///home/acceso/Imágenes/fondos_pantalla/" # tambien se puede obtener con os.path
		self.lista_arch = sorted(os.listdir(self.ruta))
		print(self.lista_arch)
	
	def cambio_fondo(self):		
		self.duracion = 700 #equivalente a 10min
		self.orden = "s"
		
		#self.duracion = int(input("\nintroduzca el tiempo de duración por imagen en ms: "))
		#self.orden = input("\nReproducir en orden aleatorio(s/n): ")
		
		
		while (self.ciclo): #ciclo de repeticion infinita
			
			try:
				if(self.orden.lower() == "s"):
					time.sleep(self.duracion)
					print("."*10+"cambiando fondo de pantalla"+"."*10)
					subprocess.call("gsettings set org.gnome.desktop.background picture-uri file:{0}{1}".format(self.ruta,self.lista_arch[rd.randint(0,len(self.lista_arch)-1)]),shell =True)
				else:	
					
					if(self.ind < len(self.lista_arch)):
						time.sleep(self.duracion)
						print("."*10+"cambiando fondo de pantalla"+"."*10)
						subprocess.call("gsettings set org.gnome.desktop.background picture-uri file:{0}{1}".format(self.ruta,self.lista_arch[self.ind]),shell =True)	
					else:
						self.ind = 0
						
			except Exception as e:
				print(e)
				self.ciclo = False # al detectar un error(ej: falta una imagen) se detiene el ciclo infinito				
			
			self.ind += 1
			
#gsettings set org.gnome.desktop.background picture-uri file:///home/acceso/Imágenes/1.jpg

if(__name__ == "__main__"):
	cf = Fondo_pantalla()
	cf.cambio_fondo()
