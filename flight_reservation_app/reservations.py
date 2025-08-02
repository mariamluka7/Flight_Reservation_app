# View all reservations
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk,Image

import database

def create_view_page(root,go_home,go_booking,go_view):

    view = ctk.CTkFrame(root,fg_color='#F4F9F9')

    top_strip =ctk.CTkFrame(view,height=80,fg_color='#756AB6',corner_radius=0)
    top_strip.pack(fill='x',side='top') 

    app_title = ctk.CTkLabel(top_strip,text='ROMA Reservations ✨',text_color='#F2FCFC',bg_color="#756AB6",font=("Segoe UI",28,'bold'))
    app_title.place(x=50,y=20)

    #-------creating navigation button in strip------------------------------------
    home_lbl = ctk.CTkLabel(top_strip,text='Home',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#756AB6')
    home_lbl.place(x=1100,y=30)

    home_lbl.bind('<Button-1>',lambda event:go_home())
    #------
    booking_lbl = ctk.CTkLabel(top_strip,text='Book Flight',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#756AB6')
    booking_lbl.place(x=1200,y=30)

    booking_lbl.bind('<Button-1>',lambda event:go_booking())
    #------
    viewReserv_lbl = ctk.CTkLabel(top_strip,text='View Reservations',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#756AB6')
    viewReserv_lbl.place(x=1330,y=30)

    viewReserv_lbl.bind('<Button-1>',lambda event:go_view()) 

    textlbl = ctk.CTkLabel(view,text='Your Reservations',font=("Segoe UI",30,'bold'),text_color='#645CAA')
    textlbl.place(relx=0.2,rely=0.2)

    # frame for showing reservations 
    reservations_frame = ctk.CTkFrame(view,fg_color='white',border_color='#756AB6',corner_radius=10,border_width=2,
                                      width=900,height=500)
    reservations_frame.place(relx=0.2,rely=0.3) 
    reservations_frame.pack_propagate(False)

    book_btn = ctk.CTkButton(view,text='Book New Flight',font=("Segoe UI",16),fg_color='#645CAA',
                             corner_radius=8,cursor='hand2',text_color='white',width=65,height=37,command=go_booking)
    book_btn.place(relx=0.7,rely=0.22)

    def onhover_enter(event):
        book_btn.configure(fg_color='#553C8B')

    def onhover_leave(event):
        book_btn.configure(fg_color='#645CAA')

    book_btn.bind('<Enter>',onhover_enter)
    book_btn.bind('<Leave>',onhover_leave)

    # display database using treeview 
    columns = ['Flight Number','Name','Departure','Destination','Date','Seat']
    tree = ttk.Treeview(reservations_frame,columns=columns,show='headings',height=15) 

    for col in columns:
        tree.heading(col,text=col)
        tree.column(col,anchor='center',stretch=False,width=190)

    tree.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)

    scroll = ttk.Scrollbar(reservations_frame,orient='vertical',command=tree.yview)
    scroll.grid(row=0,column=1,sticky='ns')
    tree.configure(yscrollcommand=scroll.set)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Segoe UI', 16, 'bold'),foreground="#4C4584")
    style.configure("Treeview", font=('Segoe UI', 14), rowheight=40)

    reservations_frame.grid_rowconfigure(0,weight=1)
    reservations_frame.grid_columnconfigure(0,weight=1) 

    reservations = database.show_all() 


    # to ensure the view table updates and use it in main 
    def refresh_table():

        for row in tree.get_children():
            tree.delete(row)

        updated_revs = database.show_all()

        for res in updated_revs:
            tree.insert('','end',values=res) 


    return view , refresh_table 
