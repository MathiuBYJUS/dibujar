from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog

root=Tk()
root.title("Dibujar")
root.geometry("400x400")
root.config(bg="lightgreen")

input_1=Entry(root)
input_1.place(relx=0.5 , rely=0.2 , anchor=CENTER)
label_1=Label(root,text="Dibujar")
label_1.place(relx=0.5 , rely=0.1 , anchor=CENTER)
canvas_1=Canvas(root,width=400,height=400,bg="lightblue",highlightthickness=3)
canvas_1.place(relx=0.5 , rely=0.5,anchor=CENTER)
image_1=ImageTk.PhotoImage(Image.open("start_point1.png"))
createImage=canvas_1.create_image(20,20,image=image_1)
var_1=""
Inicial_X=20
Inicial_Y=20
Final_X=20
Final_Y=20
def a():
    
    global var_1
    global Inicial_X
    global Inicial_Y
    global Final_X
    global Final_Y
    Final_X=Inicial_X
    Final_Y=Inicial_Y
    Final_X=Final_X + 5
    var_1="right"
    draw(var_1,Inicial_X,Inicial_Y,Final_X,Final_Y)
    
def b():
    
    global var_1
    global Inicial_X
    global Inicial_Y
    global Final_X
    global Final_Y
    Final_X=Inicial_X
    Final_Y=Inicial_Y
    Final_X=Final_X - 5
    var_1="left"
    draw(var_1,Inicial_X,Inicial_Y,Final_X,Final_Y)
    
    
def c():
    
    global var_1
    global Inicial_X
    global Inicial_Y
    global Final_X
    global Final_Y
    Final_Y=Inicial_Y
    Final_X=Inicial_X
    Final_Y=Final_Y - 5
    var_1="up"
    draw(var_1,Inicial_X,Inicial_Y,Final_X,Final_Y)
    
def d():
    
    global var_1
    global Inicial_X
    global Inicial_Y
    global Final_X
    global Final_Y
    Final_Y=Inicial_Y
    Final_X=Inicial_X
    Final_Y=Final_Y + 5
    var_1="down"
    draw(var_1,Inicial_X,Inicial_Y,Final_X,Final_Y)
    
def draw(var_1,Inicial_X,Inicial_Y,Final_X,Final_Y):
    f=input_1.get()
    if keypress=="D":
        draw_line=canvas_1.create_line(var_1,Inicial_X,Inicial_Y,Final_X,Final_Y,fill=f)
            
        
    if keypress=="A":
        draw_line=canvas_1.create_line(var_1,Inicial_X,Inicial_Y,Final_X,Final_Y,fill=f)
        
    if keypress=="W":
        draw_line=canvas_1.create_line(var_1,Inicial_X,Inicial_Y,Final_X,Final_Y,fill=f)
        
    if keypress=="S":
         draw_line=canvas_1.create_line(var_1,Inicial_X,Inicial_Y,Final_X,Final_Y,fill=f)
    
root.bind("<D>",a)
root.bind("<A>",b)
root.bind("W>",c)   
root.bind("<S>",d)
  
root.mainloop()

