# main application file
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk,Image
import os , sys 

import home,reservations,booking 

# Function to ensure the .exe file can reach images and logo 
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception :
        base_path = os.path.abspath(".") 

    return os.path.join(base_path,relative_path) 
#----------------------------------------------------------

ctk.set_appearance_mode("system")      # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Also "green", "dark-blue", or your own JSON theme

root = ctk.CTk()
root.title('Flight Reservation App')
root.iconbitmap(resource_path("assets/app_logo.ico"))

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