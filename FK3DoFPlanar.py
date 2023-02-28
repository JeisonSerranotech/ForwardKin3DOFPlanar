

import customtkinter
from matplotlib import pyplot as  plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from customtkinter import CTk,CTkFrame,CTkEntry,CTkLabel,CTkButton,CTkImage
from tkinter import *
from PIL import Image
from PosFrame3DOFP import *
import numpy as np
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style

# Colores del proyecto

c_bg='#FFFFFF'
c_nja='#FD7D70'
c_gris='#70818B'

# declaracion de la ventana

main_root=CTk()
main_root.geometry('400x500+350+100')
main_root.minsize(400,500)
main_root.maxsize(480,1300)
main_root.config(bg=c_bg)

#Configuracion of columns of the grid main root

main_root.columnconfigure(0,weight=1)


#Definition of frames and widgtes

frame_photo= CTkFrame(master=main_root,fg_color=c_nja,height=32,width=400,border_width=0,border_color=c_nja)
frame_photo.grid(column=0,row=0,sticky="")
frame_photo2= CTkFrame(master=main_root,fg_color='white',height=300,width=400,border_width=0)
frame_photo2.grid(column=0,row=1,sticky="")
frame_text=CTkFrame(master=main_root,fg_color=c_bg,height=100,width=400,border_width=0)
frame_text.grid(column=0,row=2,sticky="")
frame_button=CTkFrame(master=main_root,fg_color=c_bg,height=78,width=400).grid(column=0,row=3,sticky="")


label_1=CTkLabel(frame_photo,text="FORWAD KN APP",text_color='white',width=144,height=19,font=('Work Sans',15,'bold'))
label_1.grid(column=0,row=0,sticky="")
frame_photo.grid_propagate(False)
label_1.place(relx=0.5, rely=0.5, anchor='center')
label_title=CTkLabel(frame_text,text="Ready to do some math?",text_color=c_nja,width=238,height=22,font=('Work Sans extrabold',19,'bold'))
label_title.grid(column=0,row=0,sticky="")
label_header=CTkLabel(frame_text,text="This Apps helps you to calculate the position \n relative to the base frame for your 3DOF planar\nrobot.",text_color=c_gris,width=268,height=45,font=('Work Sans',14))
label_header.grid(column=0,row=1,pady=10,sticky="")
myfont=customtkinter.CTkFont('Works Sans',16,"bold")

#definicion de funcion abrir nueva ventana



def abrirventana() :
    
    
    def cpt_value():
        Val_a =float(entry_a.get())
        Val_b= float(entry_b.get())
        Val_c= float(entry_c.get())
        P_final=position(Val_a,Val_b,Val_c)
        label_x = CTkLabel(master=nuevaroot, text=P_final[0, 0], text_color='black', width=50, height=19,
                           font=('Work Sans', 15))
        label_x.place(x=250,y=250)
        label_y = CTkLabel(master=nuevaroot, text=P_final[1, 0], text_color='black', width=50, height=19,
                       font=('Work Sans', 15))
        label_y.place(x=250, y=280)
        label_text_x = CTkLabel(master=nuevaroot, text='Position X {0}= ', text_color='black', width=50, height=19,
                           font=('Work Sans', 15, 'bold'))
        label_text_x.place(x=130, y=250)
        label_text_y = CTkLabel(master=nuevaroot, text='Position Y {0}= ', text_color='black', width=50, height=19,
                                font=('Work Sans', 15, 'bold'))
        label_text_y.place(x=130, y=280)




        
        
    nuevaroot=Toplevel(main_root)
    nuevaroot.geometry('520x420')
    nuevaroot.title("Calculo de variables de posicion respecto a frame base")
    nuevaroot.config(bg='white')

    frame_pr = CTkFrame(master=nuevaroot, fg_color=c_nja, height=32, width=620, border_width=0, border_color=c_nja)
    frame_pr.grid(column=0, row=0, sticky="")
    frame_tx = CTkFrame(master=nuevaroot, fg_color='white', height=200, width=620, border_width=0,corner_radius=4)
    frame_tx.grid(column=0,row=1,sticky="")
    frame_a = CTkFrame(master=frame_tx,fg_color='#EAEAEA',width=151,height=67,corner_radius=15)
    frame_a.place(x=20,y=35)
    frame_b = CTkFrame(master=frame_tx, fg_color='#EAEAEA', width=151, height=67, corner_radius=15)
    frame_b.place(x=20, y=124)
    frame_c = CTkFrame(master=frame_tx, fg_color='#EAEAEA', width=151, height=67, corner_radius=15)
    frame_c.place(x=230, y=35)
    btn_cl = CTkButton(master=frame_tx, fg_color=c_nja, text="Calcular", text_color=c_bg, width=175,
                         height=45, font=myfont,command=cpt_value)
    lbl_angulo_a=CTkLabel(frame_a,text="Theta A",text_color='#70818B',width=68,height=11,font=('Open Sans',14,'bold'))
    lbl_angulo_a.place(x=8,y=10)
    lbl_angulo_b = CTkLabel(frame_b, text="Theta B", text_color='#70818B', width=68, height=11,
                            font=('Open Sans', 14, 'bold'))
    lbl_angulo_b.place(x=8, y=10)
    lbl_angulo_c = CTkLabel(frame_c, text="Theta C", text_color='#70818B', width=68, height=11,
                            font=('Open Sans', 14, 'bold'))
    lbl_angulo_c.place(x=8, y=10)
    label_front = CTkLabel(frame_pr, text="INPUT VALUES", text_color='white', width=144, height=19,
                       font=('Work Sans', 15, 'bold'))
    label_front.grid(column=0, row=0, sticky="")
    frame_pr.grid_propagate(False)




    # Entrys

    entry_a=CTkEntry(frame_a,font=('Opens sans',12,'bold'),width=122,height=30,fg_color='white',placeholder_text="Valor en Degrees",placeholder_text_color="#70818B")
    entry_a.place(x=8,y=30)
    entry_b = CTkEntry(frame_b, font=('Opens sans', 12, 'bold'), width=122, height=30, fg_color='white',
                       placeholder_text="Valor en Degrees", placeholder_text_color="#70818B")
    entry_b.place(x=8, y=30)
    entry_c = CTkEntry(frame_c, font=('Opens sans', 12, 'bold'), width=122, height=30, fg_color='white',
                       placeholder_text="Valor en Degrees", placeholder_text_color="#70818B")
    entry_c.place(x=8, y=30)
    btn_cl.place(x=220,y=130)
    nuevaroot.columnconfigure(0,weight=1)

    #Captura de valores







btn_main=CTkButton(master=frame_button,fg_color=c_nja,text="Let's get started",text_color=c_bg,width=175,height=45,font=myfont,command=abrirventana)
btn_main.grid(column=0,row=3,sticky="")

#Creating the image

img_robot=my_image = CTkImage(Image.open("./images/Mainpagge.png"),size=(200, 280))
frame_photo.label=CTkLabel(master=frame_photo2,image=img_robot,width=400,height=300,text="")
frame_photo.label.grid(column=0,row=0,sticky="")

#Ventana nueva posicionando los labels y entrys para que se pueda almacenar la informacion




main_root.mainloop()
