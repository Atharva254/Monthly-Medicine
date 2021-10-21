from time import strftime
from tkinter.font import BOLD, ITALIC
from Med_functions import *
from tkinter import *
from tkinter.ttk import *
from tkinter.constants import CENTER, E, RIGHT, W
from datetime import date
import PIL.Image as im
import PIL.ImageTk as itk
if __name__ == "__main__":

    root = Tk()

    #ROOT GEOMETRY====================================================

    screen_w=1366
    screen_h=768

    window_w=400
    window_h=500

    position_x= int(screen_w/2 - window_w/2)
    position_y= int(screen_h/3 - window_h/3)
    root.title("Medicine system")
    root.geometry("{}x{}+{}+{}".format(window_w,window_h,position_x,position_y))
    root.resizable(height=False,width=False)
    #BACKGROUND IMAGE==============================================
    image = im.open("BG 1.png")
    if image.size != (window_w, window_h):
        image = image.resize((window_w, window_h), im.ANTIALIAS)
    image = itk.PhotoImage(image)
    bg_label = Label(root, image = image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = image

    #BUTTONS=================================================
    style = Style()
    style.configure("Button_style1.TButton", foreground="black", background="white",font=(BOLD,13,ITALIC))
    style.configure("Button_style2.TButton", foreground="black", background="red",font=(BOLD))
    style.configure("Button_style3.TButton", foreground="black", background="green",font=(BOLD))
    button_1= Button(root,text=medicine_1,style="Button_style1.TButton",command=lambda mkey=medicine_1:increment(mkey))
    button_1.grid(row=0,column=0,sticky=W)

    button_2= Button(root, text=medicine_2,style="Button_style1.TButton",command=lambda mkey=medicine_2:increment(mkey))
    button_2.grid(row=1,column=0,sticky=W)

    button_3= Button(root, text=medicine_3,style="Button_style1.TButton",command=lambda mkey=medicine_3:increment(mkey))
    button_3.grid(row=2,column=0,sticky=W)
    
    button_4= Button(root, text=medicine_4,style="Button_style1.TButton",command=lambda mkey=medicine_4:increment(mkey))
    button_4.grid(row=3,column=0,sticky=W)

    button_5= Button(root, text="Reset",style="Button_style2.TButton",command=lambda mkey='reset':increment(mkey))
    button_5.place(x=150,rely=0.7)

    button_6= Button(root, text="Confirm",style="Button_style3.TButton",command=print_list)
    button_6.place(x=150,rely=0.8)

    #LABELS===================================================
    today = date.today()
    date_today = today.strftime("%B %d, %Y")
    
    style.configure("Date_label.TLabel", foreground="black", background="White",font=(BOLD,10))
    date_label= Label(root,text=date_today,style="Date_label.TLabel",justify=RIGHT)
    date_label.place(x=window_w-100,y=1)
    root.mainloop()