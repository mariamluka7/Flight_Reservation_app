# Flight booking form
from tkinter import *
from tkcalendar import Calendar
import customtkinter as ctk
from PIL import ImageTk,Image

from database import add_reserevation

cal_frame = None # initialize a frame for calendar
warning_lbl = None

def create_booking_page(root,go_home,go_booking,go_view):

    book = ctk.CTkFrame(root,fg_color='#F4F9F9')

    top_strip =ctk.CTkFrame(book,height=80,fg_color='#756AB6',corner_radius=0)
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
    
    # creating the booking page wigdets-------------------------------------------
    textlbl = ctk.CTkLabel(book,text='Book a Flight',font=('Segoe UI',32,'bold'),text_color='#645CAA')
    textlbl.place(relx=0.3,rely=0.2,anchor='w')

    inputs_frame = ctk.CTkFrame(book,corner_radius=10,fg_color='white',width=600,height=500,
                                border_color='#756AB6',border_width=2)
    inputs_frame.place(relx=0.3,rely=0.59,anchor='w')

    name_field = ctk.CTkEntry(inputs_frame,placeholder_text='Enter your full name',placeholder_text_color='gray',width=550,height=37,
                              fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2,text_color='black')
    name_field.place(relx=0.5,rely=0.15,anchor='center') 

    namelbl = ctk.CTkLabel(inputs_frame,text='Full Name',text_color='black',font=('Segoe UI',16))
    namelbl.place(relx=0.04,rely=0.043)

    flnum_field = ctk.CTkEntry(inputs_frame,placeholder_text='e.g. FS123',placeholder_text_color='gray',width=550,height=37,
                              fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2,text_color='black')
    flnum_field.place(relx=0.5,rely=0.35,anchor='center') 

    flnumlbl = ctk.CTkLabel(inputs_frame,text='Flight Number',text_color='black',font=('Segoe UI',16))
    flnumlbl.place(relx=0.04,rely=0.24)

    dep_field = ctk.CTkEntry(inputs_frame,placeholder_text='e.g. Cairo',placeholder_text_color='gray',width=260,height=37,
                              fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2,text_color='black')
    dep_field.place(relx=0.046,rely=0.5)

    deplbl = ctk.CTkLabel(inputs_frame,text='Departure',text_color='black',font=('Segoe UI',16))
    deplbl.place(relx=0.04,rely=0.43)

    dest_field = ctk.CTkEntry(inputs_frame,placeholder_text='e.g. London',placeholder_text_color='gray',width=260,height=37,
                              fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2,text_color='black')
    dest_field.place(relx=0.52,rely=0.5)

    destlbl = ctk.CTkLabel(inputs_frame,text='Destination',text_color='black',font=('Segoe UI',16))
    destlbl.place(relx=0.515,rely=0.43)

    stnum_field = ctk.CTkEntry(inputs_frame,placeholder_text='e.g. 7A',placeholder_text_color='gray',width=260,height=37,
                              fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2,text_color='black')
    stnum_field.place(relx=0.52,rely=0.69)

    stnumlbl = ctk.CTkLabel(inputs_frame,text='Seat Number',text_color='black',font=('Segoe UI',16))
    stnumlbl.place(relx=0.515,rely=0.62)

    sel_date = ctk.StringVar(value='Select a Date')

    date_field = ctk.CTkLabel(inputs_frame,textvariable=sel_date,text_color='black',width=200,height=37,
                              fg_color='#DCDCDC',corner_radius=10)
    date_field.place(relx=0.046,rely=0.69)

    datelbl = ctk.CTkLabel(inputs_frame,text='Date',text_color='black',font=('Segoe UI',16))
    datelbl.place(relx=0.04,rely=0.62)
 

    def calendar_field():

        global cal_frame
        
        #to close any open calendar frames
        if cal_frame is not None:
            cal_frame.destroy()

        cal_frame = ctk.CTkFrame(inputs_frame,height=170,width=200,fg_color='#DCDCDC')
        cal_frame.place(relx=0.4,rely=0.4)
        cal_frame.pack_propagate(False)

        cal = Calendar(cal_frame,selectmode='day',date_pattern='yyyy-mm-dd')
        cal.pack(pady=10,padx=10) 

        def select_date(event):
            selected_date = cal.get_date()
            sel_date.set(selected_date)
            cal_frame.destroy()
        
        cal.bind('<<CalendarSelected>>',select_date)

    cal_btn = ctk.CTkButton(inputs_frame,text='🗓',command=calendar_field,width=40,height=37,fg_color='#DCDCDC',
                            font=('Segoe UI',16),text_color='black')
    cal_btn.place(relx=0.4,rely=0.69)


    def confirm_booking():

        global warning_lbl

        name = name_field.get()
        flight_number = flnum_field.get()
        departure = dep_field.get()
        destination = dest_field.get()
        date = sel_date.get()
        seat_number = stnum_field.get()

        if warning_lbl is not None:
            warning_lbl.destroy()
            warning_lbl = None 

        if not all ([name,flight_number,departure,destination,seat_number]) or date == 'Select a Date':
            warning_lbl = ctk.CTkLabel(inputs_frame,text='Please fill all required input fields',text_color='red',
                                       font=('Segoe UI',16))
            warning_lbl.place(relx=0.1,rely=0.85)

        else:
            add_reserevation(name,flight_number,departure,destination,date,seat_number)

            #reset input fields
            name_field.delete(0,'end')
            flnum_field.delete(0,'end')
            dep_field.delete(0,'end')
            dest_field.delete(0,'end')
            stnum_field.delete(0,'end')
            sel_date.set('Select a Date') 

            success_lbl = ctk.CTkLabel(inputs_frame,text='Flight booked successfully !',text_color='green',
                                       font=('Segoe UI',16))
            
            success_lbl.place(relx=0.1,rely=0.85)
            success_lbl.after(3000,success_lbl.destroy) 

    confirm_btn = ctk.CTkButton(inputs_frame,text='Book Flight',fg_color='#645CAA',
                                font=('Segoe UI',14),cursor='hand2',corner_radius=8,
                                text_color='white',width=65,height=37,command=confirm_booking)
    confirm_btn.place(relx=0.8,rely=0.85)

    def onhover_enter(event):
        confirm_btn.configure(fg_color='#553C8B')

    def onhover_leave(event):
        confirm_btn.configure(fg_color='#645CAA')

    confirm_btn.bind('<Enter>',onhover_enter)
    confirm_btn.bind('<Leave>',onhover_leave)

    cancel_btn = ctk.CTkButton(inputs_frame,text='Cancel',fg_color='white',
                                font=('Segoe UI',14),cursor='hand2',corner_radius=8,
                                text_color='black',width=60,height=37,command=go_home,border_width=2,border_color='#DCDCDC')
    cancel_btn.place(relx=0.68,rely=0.85)

    def onhover_enter(event):
        cancel_btn.configure(fg_color='#DCDCDC')

    def onhover_leave(event):
        cancel_btn.configure(fg_color='white')

    cancel_btn.bind('<Enter>',onhover_enter)
    cancel_btn.bind('<Leave>',onhover_leave)
    

    return book

