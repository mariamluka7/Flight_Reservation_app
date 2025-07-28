# Home page UI
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk,Image

import reservations 

# ctk.set_appearance_mode("system")      # Options: "dark", "light", "system"
# ctk.set_default_color_theme("blue")  # Also "green", "dark-blue", or your own JSON theme

# root = ctk.CTk()
# root.title('Flight Reservation App')
# root.iconbitmap("C:/Users/Lenovo/Desktop/ASU.R/Sprints/icons/app pot. logo.ico")
# #root.configure(fg_color='#F4F9F9')

# # work around customtkinter to be able to use 'zoomed'
# def maxi():
#     root.state('zoomed')

# root.after(10,maxi)
#--------------------------------------------------------------------------------

# home_page = ctk.CTkFrame(root)
# home_page.configure(fg_color='#F4F9F9')

# book_page = ctk.CTkFrame(root)
# book_page.configure(fg_color='#F4F9F9')

# view_page = ctk.CTkFrame(root)
# view_page.configure(fg_color='#F4F9F9')

# pages = [home_page,book_page,view_page]

# for page in pages :
#     page.place(relwidth=1,relheight=1)


def create_home_page(root,go_home,go_booking,go_view):

    home = ctk.CTkFrame(root,fg_color='#F4F9F9')

    # creating upper navigation strip--------------------------------------------
    top_strip =ctk.CTkFrame(home,height=80,fg_color='#756AB6',corner_radius=0)
    top_strip.pack(fill='x',side='top') 

    app_title = ctk.CTkLabel(top_strip,text='ROMA Reservations ✨',text_color='#F2FCFC',bg_color="#756AB6",font=("Segoe UI",28,'bold'))
    app_title.place(x=50,y=20)

    #creating navigation button in strip
    home_lbl = ctk.CTkLabel(top_strip,text='Home',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#756AB6')
    home_lbl.place(x=1100,y=30)

    # def go_home(event):
    #     print('home page!!') 
    #     home.tkraise()

    home_lbl.bind('<Button-1>',lambda event:go_home())
    #------
    booking_lbl = ctk.CTkLabel(top_strip,text='Book Flight',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#756AB6')
    booking_lbl.place(x=1200,y=30)

    # def go_booking(event=None):

    #     print('booking page !!') 

    booking_lbl.bind('<Button-1>',lambda event:go_booking())
    #------
    viewReserv_lbl = ctk.CTkLabel(top_strip,text='View Reservations',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#756AB6')
    viewReserv_lbl.place(x=1330,y=30)

    # def go_view(event=None):
    #     print('viewing page !!') 
    #     reservations.create_view_page(root).tkraise() 

    viewReserv_lbl.bind('<Button-1>',lambda event:go_view())

    #------------------widgets for navigation in home page----------------------------
    wlcm_lbl = ctk.CTkLabel(home,text='Welcome to ROMA Reservations',text_color='#645CAA',font=('Segoe UI',42,'bold'))
    #wlcm_lbl.pack(pady=40)
    wlcm_lbl.place(relx=0.5,rely=0.2,anchor='center')
    #--------
    info_lbl = ctk.CTkLabel(home,text='Book your flights and manage your reservations with our simple and intuitive system.',
                            font=('Segoe UI',20))
    info_lbl.configure(wraplength=600)
    info_lbl.place(relx=0.5,rely=0.3,anchor='center')
    #-------
    #--- BOOK A FLIGHT frame with button and symbol inside-----------
    book_frame = ctk.CTkFrame(home,width=450,height=300,corner_radius=10,border_width=2,border_color='#756AB6',fg_color="white")
    book_frame.place(relx=0.48,rely=0.68,anchor='e')

    def on_enterbook(event):
        book_frame.configure(fg_color="#F6F5FF")

    def on_leavebook(event):
        book_frame.configure(fg_color="white")

    book_frame.bind('<Enter>',on_enterbook)
    book_frame.bind('<Leave>',on_leavebook)

    book_img = ctk.CTkImage(Image.open("C:/Users/Lenovo/Desktop/ASU.R/Sprints/program aesthetic/airplane.png"),
                            size=(60,60))
    book_imblabel = ctk.CTkLabel(book_frame,image=book_img,text='')
    book_imblabel.place(relx=0.5,rely=0.2,anchor='center') 

    book_text1 = ctk.CTkLabel(book_frame,text='Book a Flight',text_color='#756AB6',font=('Segoe UI',26))
    book_text1.place(relx=0.5,rely=0.4,anchor='center')

    book_text2 = ctk.CTkLabel(book_frame,text='Reserve your next flight by providing your details and flight information.',
                            font=('Segoe UI',18))
    book_text2.configure(wraplength=400)
    book_text2.place(relx=0.5,rely=0.6,anchor='center')

    book_btn = ctk.CTkButton(book_frame,text='Book Flight',font=('Segoe UI',18),
                            width=400,height=40,fg_color='#645CAA',
                            cursor='hand2',corner_radius=8,text_color='white',command=go_booking)

    def onhover_enter(event):
        book_btn.configure(fg_color='#553C8B')

    def onhover_leave(event):
        book_btn.configure(fg_color='#645CAA')

    book_btn.bind('<Enter>',onhover_enter)
    book_btn.bind('<Leave>',onhover_leave)

    book_btn.place(relx=0.5,rely=0.85,anchor='center')



    # to ensure the color changing effect is applied when mouse hovers on any widget in the frame
    for widget in book_frame.winfo_children():
        widget.bind('<Enter>',on_enterbook)
        widget.bind('<Leave>',on_leavebook)


    #--- VIEW RESERVATIONS frame with button and symbol--------------
    viewing_frame = ctk.CTkFrame(home,width=450,height=300,corner_radius=10,border_width=2,border_color='#756AB6',fg_color='white')
    viewing_frame.place(relx=0.52,rely=0.68,anchor='w')

    def on_enterview(event):
        viewing_frame.configure(fg_color="#F6F5FF")

    def on_leaveview(event):
        viewing_frame.configure(fg_color="white")

    viewing_frame.bind('<Enter>',on_enterview)
    viewing_frame.bind('<Leave>',on_leaveview)

    book_img = ctk.CTkImage(Image.open("C:/Users/Lenovo/Desktop/ASU.R/Sprints/program aesthetic/menu.png"),
                            size=(60,60))
    book_imblabel = ctk.CTkLabel(viewing_frame,image=book_img,text='')
    book_imblabel.place(relx=0.5,rely=0.2,anchor='center')

    view_text1 = ctk.CTkLabel(viewing_frame,text='View Reservations',text_color='#756AB6',font=('Segoe UI',26))
    view_text1.place(relx=0.5,rely=0.4,anchor='center')

    view_text2 = ctk.CTkLabel(viewing_frame,text='Manage your existing reservations, view details, edit or cancel if needed.',
                            font=('Segoe UI',18))
    view_text2.configure(wraplength=400)
    view_text2.place(relx=0.5,rely=0.6,anchor='center')

    view_btn = ctk.CTkButton(viewing_frame,text='View Reservations',font=('Segoe UI',18),
                            width=400,height=40,fg_color='#645CAA',
                            cursor='hand2',corner_radius=8,text_color='white',command=go_view)

    def onhover_enterv(event):
        view_btn.configure(fg_color='#553C8B')

    def onhover_leavev(event):
        view_btn.configure(fg_color='#645CAA')

    view_btn.bind('<Enter>',onhover_enterv)
    view_btn.bind('<Leave>',onhover_leavev)

    view_btn.place(relx=0.5,rely=0.85,anchor='center')

    # to ensure the color changing effect is applied when mouse hovers on any widget in the frame
    for widget in viewing_frame.winfo_children():
        widget.bind('<Enter>',on_enterview)
        widget.bind('<Leave>',on_leaveview)

    return home 


#--------------------------------------------------------------------
#----- creating top strip with logo---------------------------------------------

# root.update_idletasks() 

# screen_width = root.winfo_screenwidth

# top_strip =ctk.CTkFrame(home_page,height=80,fg_color='#756AB6',corner_radius=0)
# top_strip.pack(fill='x',side='top') 

# app_title = ctk.CTkLabel(top_strip,text='ROMA Reservations ✨',text_color='#F2FCFC',bg_color="#756AB6",font=("Segoe UI",28,'bold'))
# app_title.place(x=50,y=20)

# #-------creating navigation button in strip------------------------------------
# home_lbl = ctk.CTkLabel(top_strip,text='Home',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#756AB6')
# home_lbl.place(x=1100,y=30)

# def go_home(event):
#     print('home page!!') 
#     home_page.tkraise()

# home_lbl.bind('<Button-1>',go_home)
# #------
# booking_lbl = ctk.CTkLabel(top_strip,text='Book Flight',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#756AB6')
# booking_lbl.place(x=1200,y=30)

# def go_booking(event=None):
#     print('booking page !!') 

# booking_lbl.bind('<Button-1>',go_booking)
# #------
# viewReserv_lbl = ctk.CTkLabel(top_strip,text='View Reservations',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#756AB6')
# viewReserv_lbl.place(x=1330,y=30)

# def go_view(event=None):
#     print('viewing page !!') 
#     view_page.tkraise() 

# viewReserv_lbl.bind('<Button-1>',go_view)

# #------------------widgets for navigation in home page----------------------------
# wlcm_lbl = ctk.CTkLabel(home_page,text='Welcome to ROMA Reservations',text_color='#645CAA',font=('Segoe UI',42,'bold'))
# #wlcm_lbl.pack(pady=40)
# wlcm_lbl.place(relx=0.5,rely=0.2,anchor='center')
# #--------
# info_lbl = ctk.CTkLabel(home_page,text='Book your flights and manage your reservations with our simple and intuitive system.',
#                         font=('Segoe UI',20))
# info_lbl.configure(wraplength=600)
# info_lbl.place(relx=0.5,rely=0.3,anchor='center')
# #-------
# #--- BOOK A FLIGHT frame with button and symbol inside-----------
# book_frame = ctk.CTkFrame(home_page,width=450,height=300,corner_radius=10,border_width=2,border_color='#756AB6',fg_color="white")
# book_frame.place(relx=0.48,rely=0.68,anchor='e')

# def on_enterbook(event):
#     book_frame.configure(fg_color="#F6F5FF")

# def on_leavebook(event):
#     book_frame.configure(fg_color="white")

# book_frame.bind('<Enter>',on_enterbook)
# book_frame.bind('<Leave>',on_leavebook)

# book_img = ctk.CTkImage(Image.open("C:/Users/Lenovo/Desktop/ASU.R/Sprints/program aesthetic/airplane.png"),
#                         size=(60,60))
# book_imblabel = ctk.CTkLabel(book_frame,image=book_img,text='')
# book_imblabel.place(relx=0.5,rely=0.2,anchor='center') 

# book_text1 = ctk.CTkLabel(book_frame,text='Book a Flight',text_color='#756AB6',font=('Segoe UI',26))
# book_text1.place(relx=0.5,rely=0.4,anchor='center')

# book_text2 = ctk.CTkLabel(book_frame,text='Reserve your next flight by providing your details and flight information.',
#                           font=('Segoe UI',18))
# book_text2.configure(wraplength=400)
# book_text2.place(relx=0.5,rely=0.6,anchor='center')

# book_btn = ctk.CTkButton(book_frame,text='Book Flight',font=('Segoe UI',18),
#                          width=400,height=40,fg_color='#645CAA',
#                          cursor='hand2',corner_radius=8,text_color='white',command=go_booking)

# def onhover_enter(event):
#     book_btn.configure(fg_color='#553C8B')

# def onhover_leave(event):
#     book_btn.configure(fg_color='#645CAA')

# book_btn.bind('<Enter>',onhover_enter)
# book_btn.bind('<Leave>',onhover_leave)

# book_btn.place(relx=0.5,rely=0.85,anchor='center')



# # to ensure the color changing effect is applied when mouse hovers on any widget in the frame
# for widget in book_frame.winfo_children():
#     widget.bind('<Enter>',on_enterbook)
#     widget.bind('<Leave>',on_leavebook)


# #--- VIEW RESERVATIONS frame with button and symbol--------------
# viewing_frame = ctk.CTkFrame(home_page,width=450,height=300,corner_radius=10,border_width=2,border_color='#756AB6',fg_color='white')
# viewing_frame.place(relx=0.52,rely=0.68,anchor='w')

# def on_enterview(event):
#     viewing_frame.configure(fg_color="#F6F5FF")

# def on_leaveview(event):
#     viewing_frame.configure(fg_color="white")

# viewing_frame.bind('<Enter>',on_enterview)
# viewing_frame.bind('<Leave>',on_leaveview)

# book_img = ctk.CTkImage(Image.open("C:/Users/Lenovo/Desktop/ASU.R/Sprints/program aesthetic/menu.png"),
#                         size=(60,60))
# book_imblabel = ctk.CTkLabel(viewing_frame,image=book_img,text='')
# book_imblabel.place(relx=0.5,rely=0.2,anchor='center')

# view_text1 = ctk.CTkLabel(viewing_frame,text='View Reservations',text_color='#756AB6',font=('Segoe UI',26))
# view_text1.place(relx=0.5,rely=0.4,anchor='center')

# view_text2 = ctk.CTkLabel(viewing_frame,text='Manage your existing reservations, view details, edit or cancel if needed.',
#                           font=('Segoe UI',18))
# view_text2.configure(wraplength=400)
# view_text2.place(relx=0.5,rely=0.6,anchor='center')

# view_btn = ctk.CTkButton(viewing_frame,text='View Reservations',font=('Segoe UI',18),
#                          width=400,height=40,fg_color='#645CAA',
#                          cursor='hand2',corner_radius=8,text_color='white',command=go_view)

# def onhover_enterv(event):
#     view_btn.configure(fg_color='#553C8B')

# def onhover_leavev(event):
#     view_btn.configure(fg_color='#645CAA')

# view_btn.bind('<Enter>',onhover_enterv)
# view_btn.bind('<Leave>',onhover_leavev)

# view_btn.place(relx=0.5,rely=0.85,anchor='center')

# # to ensure the color changing effect is applied when mouse hovers on any widget in the frame
# for widget in viewing_frame.winfo_children():
#     widget.bind('<Enter>',on_enterview)
#     widget.bind('<Leave>',on_leaveview)

# home_page.tkraise() 


# root.mainloop() 
