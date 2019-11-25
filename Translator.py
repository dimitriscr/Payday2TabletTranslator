
from PIL import Image, ImageTk
import os.path
from os import path
import tkinter as tk
from functools import partial

def GetCorrespondingAchivements(EntryString):
    SearchString=EntryString.get()
    CorrespondingAchivements = []
    NumberOfCorrespondingAchivements = 0
    for i in values:
        if SearchString in i:
            NumberOfCorrespondingAchivements +=1
            CorrespondingAchivements.append(list(dict_from_file.keys())[list(dict_from_file.values()).index(i)])
    if NumberOfCorrespondingAchivements == 1:
        image2 =Image.open('Achivements\\'+CorrespondingAchivements[0]+'.PNG')
        image1 = ImageTk.PhotoImage(image2)
        photos.append(image1)
        w = image1.width()
        h = image1.height()
        AchivementCanvas.config(width=w, height=h)
        AchivementCanvas.create_image(2, 2, image=image1, anchor="nw")
    else:
        AchivementCanvas.delete('all')
         
    CorrespondingAchivementsLabel.configure(text=str(NumberOfCorrespondingAchivements)+" Corresponding Achivements")


def click(btn):
    if btn == "ap":
        RiddleEntry.insert("end","'")
    elif btn == "dg":
        RiddleEntry.insert("end","°")
    elif btn == "sm":
        RiddleEntry.insert("end",'"')
    elif btn == "pd":
        RiddleEntry.insert("end",".")
    else:
        RiddleEntry.insert("end",btn.lower())
    

    
root = tk.Tk()
root['bg'] = '#000055'


photos = []

with open('riddle.txt','r') as inf:
    dict_from_file = eval(inf.read())

keys = list(dict_from_file.keys())
values = list(dict_from_file.values())

    

sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: GetCorrespondingAchivements(sv))

RiddleEntry = tk.Entry(root)
RiddleEntry.pack()
RiddleEntry.configure(background="white", width=150,textvariable=sv)

AchivementCanvas = tk.Canvas(root)
AchivementCanvas.pack()
AchivementCanvas.configure(background='#000055', borderwidth=0, width=725, height=95)

CorrespondingAchivementsLabel = tk.Label(root, text="No Corresponing Achivements")
CorrespondingAchivementsLabel.pack()

lf = tk.LabelFrame(root, text=" keypad ", bd=3)
lf.pack(padx=15, pady=10)
btn_list = [
'A',  'B',  'C',  'D',  'E',
'F',  'G',  'H',  'I',  'J',
'K',  'L',  'M',  'N',  'O',
'P',  'Q',  'R',  'S',  'T', 'U',
'V',  'W',  'X',  'Y',  'Z',
'1',  '2',  '3',  '4',  '5',
'6',  '7',  '8',  '9',  'dg',
'pd',  'sm',  'ap']
# create and position all buttons with a for-loop
# r, c used for row, column grid values
r = 1
c = 0
n = 0
# list(range()) needed for Python3
btn = list(range(len(btn_list)))
for label in btn_list:
    # partial takes care of function and argument
    cmd = partial(click, label)
    # create the button
    path = 'Symbols\\'+label+".jpg"
    image = Image.open(path)
    photo = ImageTk.PhotoImage(image)
    photos.append(photo)
    btn[n] = tk.Button(lf, text=label, width=50, image = photo, command=cmd)
    # position the button
    btn[n].grid(row=r, column=c)
    # increment button index
    n += 1
    # update row/column position
    c += 1
    if c > 12:
        c = 0
        r += 1
root.mainloop()
