
from tkinter import *
tk=Tk()

canvas=Canvas(tk, width=500, height=400)
canvas.pack()

image1=PhotoImage(file="Pelota.png")
image2=PhotoImage(file="Arco.png")
canvas.create_image(0,100,anchor=NW, image=image1)
canvas.create_image(300,100,anchor=NW, image=image2)


def movePelota(event):
    if event.keysym == 'Left':
        canvas.move(1, -3, 0)
        print ("Posicion: ",1, canvas.create_image(0-3,100))
    else:
        canvas.move(1, 3, 0)
        print ("Posicion: ",1,canvas.create_image(0+3,100))
        
   

canvas.bind_all('<KeyPress-Left>', movePelota)
canvas.bind_all('<KeyPress-Right>', movePelota)

tk.mainloop()
