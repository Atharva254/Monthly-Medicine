from os import write
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *
medicine_1='Prolomate XL50'
medicine_2='Amlip 2.5'
medicine_3='Aspirin 75MG'
medicine_4='Refresh tears eyedrops'
value_1=0
value_2=0
value_3=0
value_4=0

medicine_data= {
    medicine_1 : value_1,
    medicine_2 : value_2,
    medicine_3 : value_3,
    medicine_4 : value_4
}


def increment(mkey):
    if mkey=='reset':
        for key in medicine_data:
            medicine_data[key] = 0
        refresh_labels(mkey)

    else:
        medicine_data[mkey]+=1
        refresh_labels(mkey)



def refresh_labels(mkey):
    if mkey=='reset':
        style = Style()
        QLabel = style.configure("LabelStyle.TLabel",font=(25))
        label2=Label(QLabel, text=medicine_data[medicine_1])
        label2.grid(row=0,column=1)
        label3=Label(text=medicine_data[medicine_2])
        label3.grid(row=1,column=1)
        label3=Label(text=medicine_data[medicine_3])
        label3.grid(row=2,column=1)
        label4=Label(text=medicine_data[medicine_4])
        label4.grid(row=3,column=1)
    else:
        if mkey==medicine_1:
            label_row=0
        elif mkey==medicine_2:
            label_row=1
        elif mkey==medicine_3:
            label_row=2
        elif mkey==medicine_4:
            label_row=3
        label1=Label(text=medicine_data[mkey])
        label1.grid(row=label_row,column=1)
    
def print_list():
    with open('Medicine List.txt','w') as data:
        for key in medicine_data:
            if medicine_data[key] != 0:
                data.write(str('{} : {}\n'.format(key,medicine_data[key])))
