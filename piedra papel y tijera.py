from tkinter import *
import random


#ventana

root = Tk() #objeto
root.geometry("400x400") #establecer a y h de la ventana
root.resizable(0,0) #de esta manera podemos cambiar tamaño ventana
root.title("Juego-Piedra, papel y tijera")
root.config(bg ='seashell3')

#texto anclado
Label(root, text = "Roca, papel y tijera", font="arial 20 bold", bg= "seashell2").pack()

#usuario eleccion

user_take = StringVar ()

Label(root, text = "Escoje tu opcion: Roca, papel, tijera", font="arial 15 bold", bg= "seashell2").place(x = 20,y=70)
Entry(root, font = "arial 15", textvariable = user_take , bg = "antiquewhite2").place(x=80 , y = 120) #place escojes una posicion especifica



#computadora

maquina = random.randint(1,3)
if maquina == 1:
    maquina= "roca"
elif maquina == 2:
    maquina= "papel"
else:
    maquina = "tijera"


#funcion para inicio de juego

Result = StringVar() #crea variable tipo texto
def play(): 
    user_eleccion = user_take.get() #recibe datos del usuario
    if user_eleccion == maquina:
        Result.set("Escojieron lo mismo, empate xD")
    #elif perdedor
    elif user_eleccion == "roca" and maquina == "papel":
        Result.set("Haz perdido, termineitor saco papel y tu piedra, perdedor")
    elif user_eleccion == "papel" and maquina == "tijera":
        Result.set("Haz perdido, termineitor saco tijera y tu papel, perdedor")
    elif user_eleccion == "tijera" and maquina == "roca":
        Result.set("Haz perdido, termineitor saco roca y tu tijera, perdedor")
    #elif ganador
    elif user_eleccion == "papel" and maquina == "roca":
        Result.set("Haz ganado tio, termineitor saco roca y tu papel, winer")
    elif user_eleccion == "tijera" and maquina == "papel":
        Result.set("Haz ganado, termineitor saco papel y tu tijera, winer")
    elif user_eleccion == "roca" and maquina == "tijera":
        Result.set("Haz ganado, termineitor saco tijera y tu roca, winer")
    #elif contra errores de eleccion
    else:
        Result.set("Invalido: Escoje una de las opciones, no trates de romper el programa, buscando bugs")
       


#funcion para resetear el juego

def reinicio():
    Result.set("")
    user_take.set("")


#funcion para salir

def Exit():
    root.destroy()



#botones

Entry(root, font = "arial 10 bold", textvariable = Result, bg = "antiquewhite2", width = 50).place(x=25 , y = 250) #place escojes una posicion especifica

Button(root, font = "arial 13 bold", text = "PLAY"  , padx = 5,bg = "seashell4", command = play).place(x=150 , y = 190) #place escojes una posicion especifica

Button(root, font = "arial 13 bold", text = "RESET"  , padx = 5,bg = "seashell4", command = reinicio).place(x=70 , y = 310) #place escojes una posicion especifica

Button(root, font = "arial 13 bold", text = "EXIT"  , padx = 5,bg = "seashell4", command = Exit).place(x=230 , y = 310) #place escojes una posicion especifica

#Enlazar eventos de teclas a activacion de funciones

root.bind("<Return>", lambda _: play())
root.bind("<Delete>", lambda _: reinicio())
root.bind("<Escape>", lambda _: Exit())




root.mainloop()












        















    






