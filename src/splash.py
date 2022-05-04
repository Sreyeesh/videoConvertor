from tkinter import *
import ttkbootstrap as ttk

splash_root = Tk()
splash_root.title("VideoConvertor Splash Screen!!")
splash_root.geometry("300x200")

splash_label = Label(splash_root, text= "VideoConvertor", font = ("None",18)) 
splash_label.pack(pady=20)
style = ttk.Style("darkly")

def main_window():
     splash_root.destroy()
     root = Tk()
     root.title('VideoConvertor - Splash Screens')
     root.geometry("500x550")

#Splash Screen Timer
splash_root.after(3000,main_window)
mainloop()
     

        
   
    