from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk 

root = Tk()
root.title("Shapes on Canvas")
root.geometry("1000x800")

canvas = Canvas(root, width = 990, height = 690, bg = "white", highlightbackground = "lightgray", relief = FLAT)
canvas.pack()

startx = Label(root, text = "Start X")
startx.place(relx = 0.1, rely = 0.9, anchor = CENTER)

startx_input = Entry(root)  
startx_input.place(relx = 0.2, rely = 0.9, anchor = CENTER)

starty = Label(root, text = "Start Y")
starty.place(relx = 0.3, rely = 0.9, anchor = CENTER)

starty_input = Entry(root)
starty_input.place(relx = 0.4, rely = 0.9, anchor = CENTER)

endx = Label(root, text = "End X")
endx.place(relx = 0.5, rely = 0.9, anchor = CENTER)

endx_input = Entry(root)
endx_input.place(relx = 0.6, rely = 0.9, anchor = CENTER)

endy = Label(root, text = "End Y")
endy.place(relx = 0.7, rely = 0.9, anchor = CENTER)

endy_input = Entry(root)
endy_input.place(relx = 0.8, rely = 0.9, anchor = CENTER)

colour = Label(root, text = "Choose Colour")
colour.place(relx = 0.4, rely = 0.95 )

colour_input = Entry(root)
colour_input.insert(0,"black")
colour_input.place(relx = 0.5, rely = 0.95)

def circle(event):
    oldx = startx_input.get()
    oldy = starty_input.get()
    newx = endx_input.get()
    newy = endy_input.get()
    keypress = "c"
    draw(keypress, oldx, oldy, newx, newy)
    
def rect(event):
    oldx = startx_input.get()
    oldy = starty_input.get()
    newx = endx_input.get()
    newy = endy_input.get()
    keypress = "r"
    draw(keypress, oldx, oldy, newx, newy)
    
    
def line(event):
    oldx = startx_input.get()
    oldy = starty_input.get()
    newx = endx_input.get()
    newy = endy_input.get()
    keypress = "i"
    draw(keypress, oldx, oldy, newx, newy)
    


root.bind("<c>", circle)
root.bind("<C>", circle)

root.bind("<r>", rect)
root.bind("<R>", rect)

root.bind("<i>", line)
root.bind("<I>", line)

def draw(keypress, oldx, oldy, newx, newy):
    color = colour_input.get()
    if keypress == "c":
        d_c = canvas.create_oval(oldx, oldy, newx, newy, fill = color)
        
    if keypress == "r":
        d_r = canvas.create_rectangle(oldx, oldy, newx, newy, fill = color)
    
    if keypress == "i":
        d_l = canvas.create_line(oldx, oldy, newx, newy, fill = color)



root.mainloop()