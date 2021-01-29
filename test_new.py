from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from random import*
from csv import *
import sys
import os
import turtle
f = Tk()
f.title("e-guarantee system")
cus_no = StringVar()
cus_name_TH = StringVar()
cus_name_EN = StringVar()
email = StringVar()
tel = StringVar()
add_no = StringVar()
add_soi = StringVar()
add_moo = StringVar()
add_vill = StringVar()
add_vill_no = StringVar()
add_buiding = StringVar()
add_tom = StringVar()
add_amp = StringVar()
add_rd = StringVar()
add_city =StringVar()
add_Pos_code = StringVar()
cer_no = StringVar()
send_date = StringVar()
spec = StringVar()
branch = StringVar()
note = StringVar()
damaged = StringVar()
##part customer##
l_cus_no = Label(f,text="รหัสลูกค้า",font=("Leelawadee UI",15))
l_cus_no.configure(background='#BDDAE6',fg='#022E5A')
l_cus_no.place(x=10,y=10)
e_cus_no = Entry(f,textvariable=cus_no,font=("Leelawadee UI",13))
e_cus_no.configure(background='#FCEDBE',fg='#022E5A')
e_cus_no.place(x=190,y=10,width=250,height=30)
l_cus_name_TH = Label(f,text="ชื่อลูกค้าภาษาไทย",font=("Leelawadee UI",15))
l_cus_name_TH.configure(background='#BDDAE6',fg='#022E5A')
l_cus_name_TH.place(x=10,y=50)
e_cus_name_TH = Entry(f,textvariable=cus_name_TH,font=("Leelawadee UI",13))
e_cus_name_TH.configure(background='#FCEDBE',fg='#022E5A')
e_cus_name_TH.place(x=190,y=50,width=250,height=30)
l_cus_name_EN = Label(f,text="ชื่อลูกค้าภาษาอังกฤษ",font=("Leelawadee UI",15))
l_cus_name_EN.configure(background='#BDDAE6',fg='#022E5A')
l_cus_name_EN.place(x=10,y=90)
e_cus_name_EN = Entry(f,textvariable=cus_name_EN,font=("Leelawadee UI",13))
e_cus_name_EN.configure(background='#FCEDBE',fg='#022E5A')
e_cus_name_EN.place(x=190,y=90,width=250,height=30)
l_email = Label(f,text="อีเมล",font=("Leelawadee UI",15))
l_email.configure(background='#BDDAE6',fg='#022E5A')
l_email.place(x=10,y=130)
e_email = Entry(f,textvariable=email,font=("Leelawadee UI",13))
e_email.configure(background='#FCEDBE',fg='#022E5A')
e_email.place(x=100,y=130,width=250,height=30)
l_tel = Label(f,text="เบอร์ติดต่อ",font=("Leelawadee UI",15))
l_tel.configure(background='#BDDAE6',fg='#022E5A')
l_tel.place(x=370,y=130)
e_tel= Entry(f,textvariable=tel,font=("Leelawadee UI",13))
e_tel.configure(background='#FCEDBE',fg='#022E5A')
e_tel.place(x=480,y=130,width=120,height=30)
l_address = Label(f,text="ที่อยู่",font=("Leelawadee UI",15))
l_address.configure(background='#BDDAE6',fg='#022E5A')
l_address.place(x=10,y=170)
l_add_no = Label(f,text="บ้านเลขที่",font=("Leelawadee UI",15))
l_add_no.configure(background='#BDDAE6',fg='#022E5A')
l_add_no.place(x=30,y=210)
e_add_no = Entry(f,textvariable=add_no,font=("Leelawadee UI",13))
e_add_no.configure(background='#FCEDBE',fg='#022E5A')
e_add_no.place(x=120,y=210,width=60,height=30)
l_add_soi = Label(f,text="ซอย",font=("Leelawadee UI",15))
l_add_soi.configure(background='#BDDAE6',fg='#022E5A')
l_add_soi.place(x=200,y=210)
e_add_soi = Entry(f,textvariable=add_soi,font=("Leelawadee UI",13))
e_add_soi.configure(background='#FCEDBE',fg='#022E5A')
e_add_soi.place(x=250,y=210,width=100,height=30)
l_add_tom = Label(f,text="แขวง/ตำบล",font=("Leelawadee UI",15))
l_add_tom.configure(background='#BDDAE6',fg='#022E5A')
l_add_tom.place(x=370,y=210)
e_add_tom = Entry(f,textvariable=add_tom,font=("Leelawadee UI",13))
e_add_tom.configure(background='#FCEDBE')
e_add_tom.place(x=480,y=210,width=100,height=30)
l_add_amp = Label(f,text="เขต/อำเภอ",font=("Leelawadee UI",15))
l_add_amp.configure(background='#BDDAE6',fg='#022E5A')
l_add_amp.place(x=590,y=210)
e_add_amp = Entry(f,textvariable=add_amp,font=("Leelawadee UI",13))
e_add_amp.configure(background='#FCEDBE',fg='#022E5A')
e_add_amp.place(x=700,y=210,width=100,height=30)
l_add_rd = Label(f,text="ถนน",font=("Leelawadee UI",15))
l_add_rd.configure(background='#BDDAE6',fg='#022E5A')
l_add_rd.place(x=30,y=250)
e_add_rd = Entry(f,textvariable=add_rd,font=("Leelawadee UI",13))
e_add_rd.configure(background='#FCEDBE',fg='#022E5A')
e_add_rd.place(x=80,y=250,width=90,height=30)
l_add_city = Label(f,text="จังหวัด",font=("Leelawadee UI",15))
l_add_city.configure(background='#BDDAE6',fg='#022E5A')
l_add_city.place(x=180,y=250)
e_add_city = Entry(f,textvariable=add_city,font=("Leelawadee UI",13))
e_add_city.configure(background='#FCEDBE',fg='#022E5A')
e_add_city.place(x=250,y=250,width=100,height=30)
l_add_Pos_code = Label(f,text="รหัสไปรษณีย์",font=("Leelawadee UI",15))
l_add_Pos_code.configure(background='#BDDAE6',fg='#022E5A')
l_add_Pos_code.place(x=370,y=250)
e_add_Pos_code= Entry(f,textvariable=add_Pos_code,font=("Leelawadee UI",13))
e_add_Pos_code.configure(background='#FCEDBE',fg='#022E5A')
e_add_Pos_code.place(x=480,y=250,width=80,height=30)
##
##part bureau##
l_cer_no = Label(f,text="รหัสใบประกัน",font=("Leelawadee UI",15))
l_cer_no.configure(background='#BDDAE6',fg='#022E5A')
l_cer_no.place(x=570,y=10)
e_cer_no = Entry(f,textvariable=cer_no,font=("Leelawadee UI",13))
e_cer_no.configure(background='#FCEDBE',fg='#022E5A')
e_cer_no.place(x=680,y=10,width=130,height=30)
l_branch = Label(f,text="สาขา",font=("Leelawadee UI",15))
l_branch.configure(background='#BDDAE6',fg='#022E5A')
l_branch.place(x=570,y=50)
e_branch = Entry(f,textvariable=branch,font=("Leelawadee UI",13))
e_branch.configure(background='#FCEDBE',fg='#022E5A')
e_branch.place(x=680,y=50,width=130,height=30)
##
##part product##
l_prod = Label(f,text="ข้อมูลสินค้า",font=("Leelawadee UI",15))
l_prod.configure(background='#BDDAE6',fg='#022E5A')
l_prod.place(x=10,y=290)
l_spec = Label(f,text="รุ่น",font=("Leelawadee UI",15))
l_spec.configure(background='#BDDAE6',fg='#022E5A')
l_spec.place(x=30,y=330)
##e_spec = Entry(f,textvariable=spec,font=("Leelawadee UI",13))
e_spec = ttk.Combobox (f,textvariable = spec, value=("","DELL INSPIRON 3593-W566055131OPPTHW10(BLACK)","HP PAVILION 15-EC0033AX (ULTRA VIOLET)", "LENOVO IDEAPAD 330-14AST-81D5007MTA (BLACK)", "HP PAVILION 15-CS3016TX (SILVER)","LENOVO-IDEAPAD-L340-15API-81LW003UTA--PLATINUM-GRAY"
,"LENOVO-IDEAPAD-S540-14IML-81NF002STA--MINERAL-GRAY"
,"LENOVO IDEAPAD S540-14IML-81NF002TTA (MINERAL GRAY)"
,"DELL INSPIRON 3581-W566015150OPPTHW10 (WHITE)"
,"HP 15-DB1049AU (SILVER)"
,"ACER ASPIRE 3 A314-41-63TQ (BLACK)"
,"ACER ASPIRE 3 A315-55G-731K (BLACK)"
,"ACER ASPIRE 3 A315-55G-53CJ (BLACK)"
,"DELL INSPIRON 5593-W566053454THW10 (SILVER)"
,"ACER ASPIRE 3 A315-55G-550G (BLACK)"
,"HP 14-CM0112AU (BLACK)"
,"DELL INSPIRON 5391-W566051012PTHW10 (SILVER)"
,"LENOVO IDEAPAD L340-15IRH-81LK00MMTA (BLACK)"
,"ASUS VIVOBOOK A571GT-AL198T"
,"HP 14S-DQ0000TU (SILVER)"
,"HP 15S-FQ1012TU (SILVER)"
,"HP 15S-FQ1001TU (SILVER)"
,"HP 14S-DK0110AU (SILVER)"
,"ASUS VIVOBOOK 15 X512DA-EJ767T (TRANSPARENT SILVER)"
,"ASUS VIVOBOOK 15 X512DA-EJ769T (PEACOCK BLUE)"
,"HP PAVILION GAMING 15-DK0207TX (GREEN)"
,"HP PAVILION GAMING 15-DK0206TX (ULTRA VIOLET)"
,"HP PAVILION GAMING 15-DK0205TX (ULTRA VIOLET)"
,"HP PAVILION GAMING 15-DK0204TX (GREEN)"
,"HP 15-DB1048AU (SILVER)"
,"ASUS LAPTOP 15 M509DA-EJ085T (SILVER)"
,"ASUS VIVOBOOK 14 X412DA-EK337T (SLATE GRAY)"
,"ASUS VIVOBOOK 14 X412DA-EK336T (TRANSPARENT GRAY)"
),font=("Leelawadee UI",13), width=20,state='readonly')
e_spec.config(background='#FCEDBE')
e_spec.place(x=70,y=330,width=600,height=30)
e_spec.current(0)
l_damaged = Label(f,text="อาการเสีย",font=("Leelawadee UI",15))
l_damaged.configure(background='#BDDAE6',fg='#022E5A')
l_damaged.place(x=30,y=370)
e_damaged = Entry(f,textvariable=damaged,font=("Leelawadee UI",13))
e_damaged.configure(background='#FCEDBE',fg='#022E5A')
e_damaged.place(x=120,y=370,width=570,height=30)
l_note = Label(f,text="บันทึกเพิ่มเติม",font=("Leelawadee UI",15))
l_note.configure(background='#BDDAE6',fg='#022E5A')
l_note.place(x=10,y=410)
##e_note = Entry(f,textvariable=note,font=("Leelawadee UI",13))
e_note = Text(f,width=20)
e_note.config(background='#FCEDBE',fg='#022E5A')
s_start = Scrollbar(f)
s_start.place(x=430,y=450)
s_start.config(command=e_note.yview)
e_note.config(yscrollcommand=s_start.set)
e_note.place(x=30,y=450,width=400,height=170)

l_send_date = Label(f,text="วันส่งคืน",font=("Leelawadee UI",15))
l_send_date.configure(background='#BDDAE6',fg='#022E5A')
l_send_date.place(x=500,y=480)
e_send_date = Entry(f,textvariable=send_date,font=("Leelawadee UI",13))
e_send_date.configure(background='#FCEDBE',fg='#022E5A')
e_send_date.place(x=580,y=480,width=100,height=30)

def cancle():
    e_cus_no.delete(0, END) 
    e_cus_name_TH.delete(0, END) 
    e_cus_name_EN.delete(0, END) 
    e_email.delete(0, END) 
    e_tel.delete(0, END) 
    e_add_no.delete(0, END) 
    e_add_soi.delete(0, END) 
    e_add_tom.delete(0, END) 
    e_add_amp.delete(0, END) 
    e_add_rd.delete(0, END) 
    e_add_city.delete(0, END) 
    e_add_Pos_code.delete(0, END) 
    e_cer_no.delete(0, END) 
    e_branch.delete(0, END) 
    e_spec.current(0)
    e_damaged.delete(0, END) 
    e_note.delete('1.0', END) 
    e_send_date.delete(0, END)   
def save():
    if (cus_no.get() == "" or
        cus_name_TH.get() == "" or
        cus_name_EN.get() == "" or
        email.get() == "" or
        tel.get() == "" or
        add_no.get() == "" or
        add_soi.get() == ""or
        add_tom.get() == "" or
        add_amp.get() == "" or
        add_rd.get() == "" or
        add_city.get() == "" or
        add_Pos_code.get() == "" or
        cer_no.get() == ""or
        branch.get() == "" or
        spec.get() == "" or
        note.get('1.0', 'end') == "" or
        send_date.get() == ""): 
              
        messagebox.showinfo("Error", "กรอกข้อมูลไม่ครบ") 
    else:
        g_cus_no = cus_no.get()
        g_cus_name_TH = cus_name_TH.get()
        g_cus_name_EN = cus_name_EN.get()
        g_email = email.get()
        g_tel = tel.get()
        g_add_no = add_no.get()
        g_add_soi = add_soi.get()
        g_add_tom = add_tom.get()
        g_add_amp = add_amp.get()
        g_add_rd = add_rd.get()
        g_add_city = add_city.get()
        g_add_Pos_code = add_Pos_code.get()
        g_cer_no = cer_no.get()
        g_branch = branch.get()
        g_spec = spec.get()
        g_damaged = damaged.get()
        g_note = note.get('1.0', 'end')
        g_send_date = send_date.get()
        csvData = [[g_cus_no,g_cus_name_TH,g_cus_name_EN,g_email,g_tel,g_add_no,g_add_soi,g_add_tom,g_add_amp,g_add_rd,g_add_city,g_add_Pos_code,g_cer_no,g_branch,g_spec,g_damaged,g_note,g_send_date]]
        ##csvData = [s]
        with open("b.csv",'r') as f:
            r = reader(f)
            lines = list(r)
        with open("b.csv",'w') as f:
            w = writer(f,lineterminator='\n')
            w.writerows(lines)
            w.writerows(csvData) 
def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
   
##save/cancle##
b_save = Button(f,text="บันทึก",command=save,font=("Leelawadee UI",15))
b_save.configure(background='#4E98B8')
b_save.place(x=520,y=550)
b_cancle = Button(f,text="ยกเลิก",command=cancle,font=("Leelawadee UI",15))
b_cancle.configure(background='#4E98B8')
b_cancle.place(x=620,y=550)
##
menubar = Menu(f)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = restart)

filemenu.add_separator()
menubar.add_cascade(label = "File", menu = filemenu)


f.config(menu = menubar)


f.minsize(850,650)
f.maxsize(850,650)
f.configure(background='#BDDAE6')
f.mainloop()
