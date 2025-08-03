# Update functionality
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk,Image
import tkinter.messagebox as msgbox
from tkcalendar import Calendar

import database

cal_frame = None # initialize a frame for calendar
warning_lbl = None

def edit_window(frame,db_id,data,resfresh):
    edit_frame = ctk.CTkFrame(frame,corner_radius=10,fg_color='white',width=600,height=500,
                                border_color='#756AB6',border_width=2)
    edit_frame.place(relx=0.3,rely=0.59,anchor='w')

    entries = []

    name_field = ctk.CTkEntry(edit_frame,width=550,height=37,
                              fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2)
    name_field.insert(0,data[2])
    name_field.place(relx=0.5,rely=0.15,anchor='center') 
    entries.append(name_field)

    namelbl = ctk.CTkLabel(edit_frame,text='Full Name',text_color='black',font=('Segoe UI',16))
    namelbl.place(relx=0.04,rely=0.043)

    flnum_field = ctk.CTkEntry(edit_frame,width=550,height=37,
                              fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2)
    flnum_field.insert(0,data[1])
    flnum_field.place(relx=0.5,rely=0.35,anchor='center') 
    entries.append(flnum_field)

    flnumlbl = ctk.CTkLabel(edit_frame,text='Flight Number',text_color='black',font=('Segoe UI',16))
    flnumlbl.place(relx=0.04,rely=0.24)

    dep_field = ctk.CTkEntry(edit_frame,width=260,height=37,
                              fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2)
    dep_field.insert(0,data[3])
    dep_field.place(relx=0.046,rely=0.5)
    entries.append(dep_field)

    deplbl = ctk.CTkLabel(edit_frame,text='Departure',text_color='black',font=('Segoe UI',16))
    deplbl.place(relx=0.04,rely=0.43)

    dest_field = ctk.CTkEntry(edit_frame,width=260,height=37,
                              fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2)
    dest_field.insert(0,data[4])
    dest_field.place(relx=0.52,rely=0.5)
    entries.append(dest_field) 

    destlbl = ctk.CTkLabel(edit_frame,text='Destination',text_color='black',font=('Segoe UI',16))
    destlbl.place(relx=0.515,rely=0.43)

    stnum_field = ctk.CTkEntry(edit_frame,width=260,height=37,
                              fg_color='#F4F9F9',border_color="#DCDCDC",border_width=2)
    stnum_field.insert(0,data[6])
    stnum_field.place(relx=0.52,rely=0.69)
    entries.append(stnum_field) 

    stnumlbl = ctk.CTkLabel(edit_frame,text='Seat Number',text_color='black',font=('Segoe UI',16))
    stnumlbl.place(relx=0.515,rely=0.62)

    sel_date = ctk.StringVar(value=data[5])

    date_field = ctk.CTkLabel(edit_frame,textvariable=sel_date,width=200,height=37,
                              fg_color='#DCDCDC',corner_radius=10)
    date_field.place(relx=0.046,rely=0.69)
    entries.append(sel_date) 

    datelbl = ctk.CTkLabel(edit_frame,text='Date',text_color='black',font=('Segoe UI',16))
    datelbl.place(relx=0.04,rely=0.62)
 

    def calendar_field():

        global cal_frame
        
        #to close any open calendar frames
        if cal_frame is not None:
            cal_frame.destroy()

        cal_frame = ctk.CTkFrame(edit_frame,height=170,width=200,fg_color='#DCDCDC')
        cal_frame.place(relx=0.4,rely=0.4)
        cal_frame.pack_propagate(False)

        cal = Calendar(cal_frame,selectmode='day',date_pattern='yyyy-mm-dd')
        cal.pack(pady=10,padx=10) 

        def select_date(event):
            selected_date = cal.get_date()
            sel_date.set(selected_date)
            cal_frame.destroy()
        
        cal.bind('<<CalendarSelected>>',select_date)

    cal_btn = ctk.CTkButton(edit_frame,text='🗓',command=calendar_field,width=40,height=37,fg_color='#DCDCDC',
                            font=('Segoe UI',16),text_color='black')
    cal_btn.place(relx=0.4,rely=0.69)

    #--------
    def update_res():
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
            warning_lbl = ctk.CTkLabel(edit_frame,text='Please fill all required input fields',text_color='red',
                                       font=('Segoe UI',16))
            warning_lbl.place(relx=0.1,rely=0.85)

        else:
            updated_values = [e.get() for e in entries]
            database.update_flight(db_id,updated_values[1],updated_values[0], updated_values[2],
                                updated_values[3],updated_values[5],updated_values[4])
            resfresh()
            edit_frame.destroy()

    update_btn = ctk.CTkButton(edit_frame,text='Update Reservation',fg_color='#645CAA',
                                font=('Segoe UI',14),cursor='hand2',corner_radius=8,
                                text_color='white',width=80,height=37,command=update_res)
    update_btn.place(relx=0.75,rely=0.85)

    def onhover_enter(event):
        update_btn.configure(fg_color='#553C8B')

    def onhover_leave(event):
        update_btn.configure(fg_color='#645CAA')

    update_btn.bind('<Enter>',onhover_enter)
    update_btn.bind('<Leave>',onhover_leave)

    cancel_btn = ctk.CTkButton(edit_frame,text='Cancel',fg_color='white',
                                font=('Segoe UI',14),cursor='hand2',corner_radius=8,
                                text_color='black',width=60,height=37,command=edit_frame.destroy,border_width=2,border_color='#DCDCDC')
    cancel_btn.place(relx=0.63,rely=0.85)

