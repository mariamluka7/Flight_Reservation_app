# main application file
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk,Image

import home,reservations,booking 

ctk.set_appearance_mode("system")      # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Also "green", "dark-blue", or your own JSON theme

root = ctk.CTk()
root.title('Flight Reservation App')
root.iconbitmap("C:/Users/Lenovo/Desktop/ASU.R/Sprints/icons/app pot. logo.ico")
#root.configure(fg_color='#F4F9F9')

# work around customtkinter to be able to use 'zoomed'
def maxi():
    root.state('zoomed')

root.after(10,maxi)

root.update_idletasks() 

view_page , refresh_table = reservations.create_view_page(root, lambda:home_page.tkraise(),
                                                lambda:booking_page.tkraise(),
                                                lambda:(view_page.tkraise(),refresh_table())
                                            )

booking_page = booking.create_booking_page(root,lambda:home_page.tkraise(),
                                                lambda:booking_page.tkraise(),
                                                lambda:(view_page.tkraise(),refresh_table())
                                            )

home_page = home.create_home_page(root, lambda:home_page.tkraise(),
                                        lambda:booking_page.tkraise(),
                                        lambda:(view_page.tkraise(),refresh_table())
                                    ) 

pages = [home_page,view_page,booking_page] 
for page in pages:
    page.place(relwidth=1,relheight=1)

home_page.tkraise() 


root.mainloop()