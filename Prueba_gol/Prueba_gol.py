
from tkinter import *
tk=Tk()
x=0
canvas=Canvas(tk, width=500, height=400)
canvas.pack()

image1=PhotoImage(file="Pelota.png")
image2=PhotoImage(file="Arco.png")
canvas.create_image(0,100,anchor=NW, image=image1)
canvas.create_image(300,100,anchor=NW, image=image2)


def movePelota(event):
    global x
    if event.keysym == 'Left':
        canvas.move(1, -3, 0)
        x=x-3
        print("Posicion: ",x)
    else:
        canvas.move(1, 3, 0)
        x=x+3
        print("Posicion: ",x)
        if x>=300:
            print ("GOOOOOOLLLL")
        
   

canvas.bind_all('<KeyPress-Left>', movePelota)
canvas.bind_all('<KeyPress-Right>', movePelota)

tk.mainloop()
