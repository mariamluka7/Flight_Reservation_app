# Home page UI
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk,Image

ctk.set_appearance_mode("system")      # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Also "green", "dark-blue", or your own JSON theme

root = ctk.CTk()
root.title('Flight Reservation App')
root.iconbitmap("C:/Users/Lenovo/Desktop/ASU.R/Sprints/icons/app pot. logo.ico")

# work around customtkinter to be able to use 'zoomed'
def maxi():
    root.state('zoomed')

root.after(10,maxi)
#--------------------------------------------------------------------------------

#----- creating top strip with logo---------------------------------------------

root.update_idletasks()

screen_width = root.winfo_screenwidth

top_strip =ctk.CTkFrame(root,height=80,fg_color='#008DDA',corner_radius=0)
top_strip.pack(fill='x',side='top') 

app_title = ctk.CTkLabel(root,text='ROMA Reservations ✨',text_color='#F2FCFC',bg_color="#008DDA",font=("Segoe UI",28))
app_title.place(x=50,y=20)
#---------------------------------------------------------------------------------

#-------creating navigation button in strip---------------------------------------
home_lbl = ctk.CTkLabel(root,text='Home',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#008DDA')
home_lbl.place(x=1100,y=30)

def go_home(event):
    print('home page!!') 

home_lbl.bind('<Button-1>',go_home)
#------
booking_lbl = ctk.CTkLabel(root,text='Book Flight',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#008DDA')
booking_lbl.place(x=1200,y=30)

def go_booking(event):
    print('booking page !!') 

booking_lbl.bind('<Button-1>',go_booking)
#------
viewReserv_lbl = ctk.CTkLabel(root,text='View Reservations',text_color='#F2FCFC',font=('Segoe UI',18),cursor='hand2',bg_color='#008DDA')
viewReserv_lbl.place(x=1330,y=30)

def go_view(event):
    print('viewing page !!') 

viewReserv_lbl.bind('<Button-1>',go_view)

#------------------widgets for navigation in home page----------------------------
wlcm_lbl = ctk.CTkLabel(root,text='Welcome to ROMA Reservations',text_color='#008DDA',font=('Segoe UI',42,'bold'))
#wlcm_lbl.pack(pady=40)
wlcm_lbl.place(relx=0.5,rely=0.2,anchor='center')
#--------
info_lbl = ctk.CTkLabel(root,text='Book your flights and manage your reservations with our simple and intuitive system',
                        font=('Segoe UI',18))
info_lbl.configure(wraplength=500)
info_lbl.place(relx=0.5,rely=0.3,anchor='center')
#-------
#---book a flight frame with button and symbol inside-----------
book_frame = ctk.CTkFrame(root,width=400,height=300,corner_radius=10,border_width=2,border_color='#008DDA')
book_frame.place(relx=0.48,rely=0.68,anchor='e')

def on_enterbook(event):
    book_frame.configure(fg_color="#F4F9F9")

def on_leavebook(event):
    book_frame.configure(fg_color="#e0e0e0")

book_frame.bind('<Enter>',on_enterbook)
book_frame.bind('<Leave>',on_leavebook)

book_img = ctk.CTkImage(Image.open("C:/Users/Lenovo/Desktop/ASU.R/Sprints/program aesthetic/Untitled_design-removebg-preview.png"),
                        size=(60,60))
book_imblabel = ctk.CTkLabel(book_frame,image=book_img,text='')
book_imblabel.place(relx=0.5,rely=0.2,anchor='center') 


#--------




#---view reservations frame with button and symbol--------------
viewing_frame = ctk.CTkFrame(root,width=400,height=300,corner_radius=10,border_width=2,border_color='#008DDA')
viewing_frame.place(relx=0.52,rely=0.68,anchor='w')

def on_enterview(event):
    viewing_frame.configure(fg_color="#F4F9F9")

def on_leaveview(event):
    viewing_frame.configure(fg_color="#e0e0e0")

viewing_frame.bind('<Enter>',on_enterview)
viewing_frame.bind('<Leave>',on_leaveview)




root.mainloop() 
