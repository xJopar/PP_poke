from tkinter import * 
from juego import *
from vista import *

class app():
    def main():
        ventana = Tk() #Tk
        juego = Juego_Pokemon()
        ventana_main = Vista(juego, ventana)
        ventana_main.mainloop() 
        
if __name__ == '__main__':
    app.main()
