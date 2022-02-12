def Binary():
    inputn =TI1.get()
    inputnum = str(inputn)
    d = 0
    L = len(inputnum)
    for c in inputnum:
        L = L - 1
        if int(c) != 0:
            d = d + 2**L
            text = 'เลขฐานสองของ{} เท่ากับ {} \n\n'.format(inputnum,d)
    v_result.set(text)

def More():
    inputa = TI2.get()
    alltext = ''
    if inputa.isnumeric()==1:
        num = int (inputa)
        text = '{:^30}\n'.format(num)
        v2_result.set(text)
        text2 = 'เลขฐานสอง คือ {}\n'.format(bin(num))
        v3_result.set(text2)
        text3 = 'เลขฐานแปด คือ {}\n'.format(oct(num))
        v4_result.set(text3)
        text4 = 'เลขฐานสิบหก คือ {}\n'.format(hex(num))
        v5_result.set(text4)
    else:
        alltext = 'กรอกข้อมูลผิดผิด'
    v3_result.set(alltext)


#GUI#

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('400x670')
GUI.title('แปลงเลข')

FONT1 = ('Tahoma' ,20,'bold')
FONT2 = ('Tahoma' ,15)
FONT3 = ('' ,15)
FONT4 = ('' ,5)

L = ttk.Label(GUI,text ='',font = FONT4)
L.pack()
L1 = ttk.Label(GUI,text ='แปลงเลขฐานสองเป็นฐานสิบ\n',font = FONT1)
L1.pack()

v_result = StringVar()
v_result.set('ใส่เลขฐานสองที่ต้องการ\n')
R2 = ttk.Label(textvariable = v_result,font = FONT3)
R2.pack()

TI1 = ttk.Entry(GUI)
TI1.pack(ipadx=50,ipady=6)
L5 = ttk.Label(GUI,text ='',font = FONT4)
L5.pack()

B2 = ttk.Button(GUI,text='แปลง!',command= Binary)
B2.pack(ipadx=50,ipady=10)
L5 = ttk.Label(GUI,text ='-----------------------------',font = FONT1)
L5.pack()

L5 = ttk.Label(GUI,text ='',font = FONT4)
L5.pack()
L3 = ttk.Label(GUI,text ='แปลงเลขฐานสิบ\n',font = FONT1)
L3.pack()

v2_result = StringVar()
v2_result.set('')
R2 = ttk.Label(textvariable = v2_result,font = FONT3)
R2.pack()
v3_result = StringVar()
v3_result.set('ใส่เลขฐานสิบที่ต้องการ\n')
R2 = ttk.Label(textvariable = v3_result,font = FONT3)
R2.pack()
v4_result = StringVar()
v4_result.set('')
R2 = ttk.Label(textvariable = v4_result,font = FONT3)
R2.pack()
v5_result = StringVar()
v5_result.set('')
R2 = ttk.Label(textvariable = v5_result,font = FONT3)
R2.pack()

TI2 = ttk.Entry(GUI)
TI2.pack(ipadx=50,ipady=6)
L5 = ttk.Label(GUI,text ='',font = FONT4)
L5.pack()

B2 = ttk.Button(GUI,text='แปลง!',command= More)
B2.pack(ipadx=50,ipady=10)

GUI.mainloop()

