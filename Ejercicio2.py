from tkinter import *
from tkinter import ttk
import tkinter as ttk
raiz = Tk()

raiz.title("Ejercicio 2")
raiz.geometry("700x650")
raiz.config(bg="black")

#creamos los frames necesarios

frame = ttk.Frame(raiz,bg="gray40",bd=40,width=900,height=20)
#frame.pack(expand=False,fill="both",padx=0,pady=0)
frame.grid(column=0,row=0)
frame.grid_propagate("True")



#frame.pack_propagate(False)
#frame.config(border=2)

frame2 = Frame(raiz,bg="#58342c",bd=10,width=100,height=90)
#frame2.pack(pady=10,padx=50,expand=True,fill="both")
frame2.grid(column=0,row=1,sticky=W)
frame2.propagate("False") 

#Frame 1

imagen = PhotoImage(file="carrito.PNG") #cremos el objeto imagen

imagen_sub=imagen.subsample(2)
etiqueta=ttk.Label(image=imagen,borderwidth=0)
etiqueta.place(x=40, y=0)

titulo = ttk.Label(frame,text="Product management",background="gray40",font=("Arial",20),fg="white",width=100,anchor="w").grid(column=0, row=0,padx=90,pady=0)

#Frame 2
ttk.Label(frame2,text="",background="#58342c",fg="white",width=99,height=0).grid(column=1,row=0,rowspan=2,sticky=W)

id = ttk.Label(frame2,text="Id Product: ",background="#58342c",font=("Arial"),fg="white").grid(column=1,row=2,padx=0,sticky=W)
ttk.Label(frame2,text="",background="#58342c").grid(column=1,row=3)


name = ttk.Label(frame2,text="Name: ",background="#58342c",font=("Arial"),fg="white").grid(column=1,row=4,sticky=W)
ttk.Label(frame2,text="",background="#58342c").grid(column=1,row=5)

descripcion = ttk.Label(frame2,text="Description: ",background="#58342c",font=("Arial"),fg="white").grid(column=1,row=6,sticky=W)
ttk.Label(frame2,text="",background="#58342c").grid(column=1,row=7)

quantity = ttk.Label(frame2,text="quantity: ",background="#58342c",font=("Arial"),fg="white").grid(column=1,row=8,sticky=W)
ttk.Label(frame2,text="",background="#58342c").grid(column=1,row=9)

price = ttk.Label(frame2,text="price: ",background="#58342c",font=("Arial"),fg="white").grid(column=1,row=10,sticky=W)

ttk.Label(frame2,text="",background="#58342c",fg="white").grid(column=2,row=0)
ttk.Label(frame2,text="",background="#58342c",fg="white").grid(column=2,row=1)
ttk.Label(frame2,text="",background="#58342c",fg="white").grid(column=2,row=2)
ttk.Label(frame2,text="",background="#58342c",fg="white").grid(column=2,row=3)
ttk.Label(frame2,text="",background="#58342c",fg="white").grid(column=2,row=4)
ttk.Label(frame2,text="",background="#58342c",fg="white").grid(column=2,row=5)


id1 = StringVar()
identry = ttk.Entry(frame2, width=50,textvariable=id1)
identry.grid(column=3, row=2,sticky=W)
identry.config(borderwidth=0,highlightthickness=0,bg="#58342c",border=1)
identry.place(x=100,y=45)
ttk.Label(frame2,text="",background="#58342c",fg="white").grid(column=3,row=3)

name1 = StringVar()
name1entry = ttk.Entry(frame2, width=50,textvariable=name1)
name1entry.grid(column=3, row=4,padx=2,columnspan=2)
name1entry.config(borderwidth=0,highlightthickness=0,bg="#58342c",border=1)
name1entry.place(x=100,y=90)
ttk.Label(frame2,text="",background="#58342c",fg="white").grid(column=3,row=5)

des1 = StringVar()
des1entry = ttk.Entry(frame2, width=50,textvariable=des1)
des1entry.grid(column=3, row=6,padx=2,columnspan=2)
des1entry.config(borderwidth=0,highlightthickness=0,bg="#58342c",border=1)
des1entry.place(x=100,y=135)
ttk.Label(frame2,text="",background="#58342c",fg="white").grid(column=3,row=7)

qua1 = StringVar()
qua1entry = ttk.Entry(frame2, width=50,textvariable=qua1)
qua1entry.grid(column=3, row=8,padx=2,columnspan=2)
qua1entry.config(borderwidth=0,highlightthickness=0,bg="#58342c",border=1)
qua1entry.place(x=100,y=180)
ttk.Label(frame2,text="",background="#58342c",fg="white").grid(column=3,row=9)

price1 = StringVar()
price1entry = ttk.Entry(frame2, width=50,textvariable=qua1)
price1entry.grid(column=3, row=10,padx=2,columnspan=2)
price1entry.config(borderwidth=0,highlightthickness=0,bg="#58342c",border=1)
price1entry.place(x=100,y=230)
ttk.Label(frame2,text="                         ",background="#58342c",fg="white").grid(column=4,row=0)

#botones

imagen1 = PhotoImage(file="lupa1.PNG")
imagen_sub=imagen1.subsample(2)
botonNuevo1 = ttk.Button(frame2,width=40, height=40, image=imagen1,foreground="#58342c",borderwidth=0)
botonNuevo1.grid(column=5,row=0)
botonNuevo1.place(x=470, y=0)

imagen2 = PhotoImage(file="escoba4.PNG")
imagen_sub = imagen2.subsample(8)
botonNuevo2 = ttk.Button(frame2,width=40, height=40, image=imagen2,foreground="#58342c",borderwidth=0)
botonNuevo2.grid(column=6,row=0)
botonNuevo2.place(x=540, y=0)

botonNuevo3 = ttk.Button(frame2,text="BACK",background="#58342c",borderwidth=0,height=2,fg="purple",activebackground="#58342c",activeforeground="purple",font=("bold"))
botonNuevo3.grid(column=7,row=0)
botonNuevo3.place(x=610, y=0)

botonNuevo4 = ttk.Button(frame2,text="Save",background="green",borderwidth=0,height=2,fg="white",activebackground="green",activeforeground="white",font=("bold"),width=20)
botonNuevo4.grid(column=5,row=1,columnspan=2)
botonNuevo4.place(x=470, y=90)

botonNuevo5 = ttk.Button(frame2,text="Delete",background="red",borderwidth=0,height=2,fg="white",activebackground="red",activeforeground="white",font=("bold"),width=20)
botonNuevo5.grid(column=5,row=2,columnspan=2)
botonNuevo5.place(x=470, y=150)

botonNuevo6 = ttk.Button(frame2,text="Update",background="orange",borderwidth=0,height=2,fg="white",activebackground="orange",activeforeground="white",font=("bold"),width=20)
botonNuevo6.grid(column=5,row=3,columnspan=2)
botonNuevo6.place(x=470, y=210)

#Tabla

#titulotab = ttk.Label(frame2,text="idproduct",width=13).grid(column=0,row=11,pady=35,)

ids = ("idproduct","1","2","3","4","5","6")
names = ("namep","Condia","la vache quirit","hamoud boualam","Mina","Aroma","Facto")
descs = ("description","lait","fromage","boisson gaseuse","Chocolat","cafe","Facto")
quants = ("quantity","24","200","98","80","60","7000")
unites = ("unite_price","100.0","300.0","90.0","50.0","80.0","600.0")





lista = Listbox(frame2,exportselection=21)
lista.grid(column=0,row=12)
lista.place(x=5,y=300,relwidth=0.6)
lista.insert(0,*ids)

lista2 = Listbox(frame2,exportselection=21)
lista2.grid(column=0,row=12)
lista2.place(x=100,y=300,relwidth=0.3)
lista2.insert(0,*names)

lista3 = Listbox(frame2,exportselection=21)
lista3.grid(column=0,row=12)
lista3.place(x=200,y=300,relwidth=0.1)
lista3.insert(0,*descs)

lista4 = Listbox(frame2,exportselection=21)
lista4.grid(column=0,row=12)
lista4.place(x=350,y=300,relwidth=0.3)
lista4.insert(0,*quants)


lista5 = Listbox(frame2,exportselection=21)
lista5.grid(column=0,row=12)
lista5.place(x=450,y=300,relwidth=0.09)
lista5.insert(0,*unites)


barra = Scrollbar(frame2,command=(lista.yview,lista2.yview,lista3.yview()))
barra.place(relx=0.7,y=300,relheight=0.097)

lista.config(yscrollcommand=barra)

ttk.Label(frame2,text="",background="#58342c",fg="white",width=0,height=100).grid(column=0,row=13,rowspan=2)

raiz.mainloop()#main para interpretar el programa