# View all reservations
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk,Image
import tkinter.messagebox as msgbox

import database
from edit_reservation import edit_window

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

    book_btn = ctk.CTkButton(view,text='Book New Flight',font=("Segoe UI",14),fg_color='#645CAA',
                             corner_radius=8,cursor='hand2',text_color='white',width=65,height=37,command=go_booking)
    book_btn.place(relx=0.73,rely=0.22)

    def onhover_enter(event):
        book_btn.configure(fg_color='#553C8B')

    def onhover_leave(event):
        book_btn.configure(fg_color='#645CAA')

    book_btn.bind('<Enter>',onhover_enter)
    book_btn.bind('<Leave>',onhover_leave)

    # display database using treeview 
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Segoe UI', 16, 'bold'),foreground="#4C4584")
    style.configure("Treeview", font=('Segoe UI', 14), rowheight=40)

    columns = ['id','Flight Number','Name','Departure','Destination','Date','Seat']
    tree = ttk.Treeview(reservations_frame,columns=columns,show='headings',height=15) 

    for col in columns:
        tree.heading(col,text=col)
        if col == 'id':
            tree.column(col,width=0,stretch=False)
        else:
            tree.column(col,anchor='center',stretch=False,width=190)

    tree.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)

    scroll = ttk.Scrollbar(reservations_frame,orient='vertical',command=tree.yview)
    scroll.grid(row=0,column=1,sticky='ns')
    tree.configure(yscrollcommand=scroll.set)

    reservations_frame.grid_rowconfigure(0,weight=1)
    reservations_frame.grid_columnconfigure(0,weight=1) 

    reservations = database.show_all() 

    # to ensure the view table updates and use it in main 
    def refresh_table():

        for row in tree.get_children():
            tree.delete(row)

        updated_revs = database.show_all()

        for res in updated_revs:
            tree.insert('','end',iid=str(res[0]),values=res) 


    search_field = ctk.CTkEntry(view,placeholder_text='Search reservations...',placeholder_text_color='gray',height=37,width=260,
                                fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2,text_color='black') 
    search_field.place(relx=0.55,rely=0.22)

    info_lbl2 = ctk.CTkLabel(view,text='To edit or delete reservations, click on the required reservation from the shown table.',
                            font=('Segoe UI', 14),text_color='black') 
    info_lbl2.configure(wraplength=250)
    info_lbl2.place(relx=0.02,rely=0.5) 

    def search_reservations():
        keyword = search_field.get() 

        results = database.flight_search(keyword) 
        for row in tree.get_children():
            tree.delete(row) 
        if not results:
            no_reslbl = ctk.CTkLabel(view,text='No Results Found',text_color='red',
                                       font=('Segoe UI',18),fg_color='white')
            no_reslbl.place(relx=0.45,rely=0.6) 
            view.after(3000,no_reslbl.destroy)
            return
        else:
            for res in results:
                tree.insert('','end',iid=str(res[0]),values=res) 
        

    search_btn = ctk.CTkButton(view,text='🔎', font=('Segoe UI', 16),height=35,width=30, fg_color='#645CAA',text_color='#F4F9F9',
                               cursor='hand2',command=search_reservations) 
    search_btn.place(relx=0.52,rely=0.22)

    def onhover_enter(event):
        search_btn.configure(fg_color='#553C8B')

    def onhover_leave(event):
        search_btn.configure(fg_color='#645CAA')

    search_btn.bind('<Enter>',onhover_enter)
    search_btn.bind('<Leave>',onhover_leave)

    def delete():
        selected_item = tree.focus()

        del_id = int(selected_item)

        confirm = msgbox.askyesno('Confirm Delete','Are you sure you want to delete this reservation ?')
        if confirm:
            database.delete_reservation(del_id)
            refresh_table() 

    def edit():
        selected_reservation = tree.focus()

        selected_info = tree.item(selected_reservation)['values'] 
        db_id = selected_reservation
        edit_window(view,db_id,selected_info,refresh_table) 
        
    edit_btn = ctk.CTkButton(view,text='✏',fg_color='white',
                                font=('Segoe UI',14),cursor='hand2',corner_radius=8,
                                text_color="green",width=30,height=37,border_width=2,border_color='green',command=edit)
    delete_btn = ctk.CTkButton(view,text='❌',fg_color='white',
                                font=('Segoe UI',14),cursor='hand2',corner_radius=8,
                                text_color="red",width=30,height=37,border_width=2,border_color='red',command=delete)
    
    def onhover_enter(event):
        edit_btn.configure(fg_color='#B2FFB5')

    def onhover_leave(event):
        edit_btn.configure(fg_color="white")

    edit_btn.bind('<Enter>',onhover_enter)
    edit_btn.bind('<Leave>',onhover_leave)

    def onhover_enter(event):
        delete_btn.configure(fg_color="#FAB9B9")

    def onhover_leave(event):
        delete_btn.configure(fg_color="white")

    delete_btn.bind('<Enter>',onhover_enter)
    delete_btn.bind('<Leave>',onhover_leave)
    
    def on_row_select(event):
        selected_res = tree.selection()

        if selected_res :
          edit_btn.place(relx=0.83,rely=0.3)
          delete_btn.place(relx=0.86,rely=0.3) 

        else:
            edit_btn.place_forget()
            delete_btn.place_forget()

    tree.bind("<<TreeviewSelect>>",on_row_select)



    return view , refresh_table 
