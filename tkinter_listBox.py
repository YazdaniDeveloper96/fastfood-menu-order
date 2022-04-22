from tkinter import *
#----------------
import os
from tkinter import font
from turtle import left
os.system('cls')
#---------------
root=Tk()
root.title("listBox wig")
#---------------------------------------root size
w=800
h=300
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))
#------------------------------------------------functions
# def func8():
#     try:
#         result=""
#         result+=str(foodList.get(foodList.curselection()))+"\n"
#         result+=str(x.get())+"\n"
#         result+=str(slider_number.get())
#         label_foods.config(text=result)
#     except:
#         label_foods.config(text="plz select food")

def func9():
    try:
        result=""
        result+=str(foodList.get(foodList.curselection()))+"\n"
        result+=str(x.get())+"\n"
        result+=str(slider_number.get())
        label_foods=Label(frame_4,text=result,font=("tahoma",6,font.BOLD),anchor=CENTER)
        label_foods.pack(fill=BOTH,pady=10)
    except:
        label_foods.config(text="plz select food")



#------------------------------------------------frames
frame_1=Frame(root,bg="#ff0000",width=200,height=300)
frame_1.pack(side=LEFT,fill=BOTH,expand=True)
frame_2=Frame(root,bg="#0000ff",width=200,height=300)
frame_2.pack(side=LEFT,fill=BOTH,expand=True)
frame_3=Frame(root,bg="#00ff00",width=50,height=300)
frame_3.pack(side=LEFT,fill=BOTH,expand=True)
frame_4=Frame(root,bg="#ffff00",width=300,height=300)
frame_4.pack(side=LEFT,fill=BOTH,expand=True)
#------------------------------------------------list of food
label_food=Label(frame_1,text="Select Food",font=("tahoma",12,font.BOLD),anchor=CENTER,bg="#ff0000",fg="#ffffff")
label_food.pack(fill=BOTH,expand=False)
foodList=Listbox(frame_1,width=12,font=("cooper balck",18,font.BOLD),bg="#ff0000",fg="#ffffff",bd=0)
foodList.insert(1,"Pizza veg")
foodList.insert(2,"Pizza met")
foodList.insert(3,"Pizza mix")
foodList.insert(4,"Pizza pep")
foodList.insert(5,"Pizza marg")
foodList.insert(6,"Sandwich chic")
foodList.insert(7,"Sandwich hot")
# foodList.config(height=foodList.size())
foodList.pack(fill=BOTH,pady=5,padx=5)
#-------------------------------------------------
# buttun_select=Button(frame_1,text="select",anchor=CENTER,bd=5,font=("tahoma",12,font.BOLD))
# buttun_select.pack(fill=BOTH,expand=True,padx=5,pady=5)
#---------------------------------------------------------size box
label_size=Label(frame_2,text="Size",anchor=CENTER,font=("tahoma",13,font.BOLD),bg="#0000ff",fg="#000000")
label_size.pack(fill=BOTH,expand=False)
x=StringVar()
list_of_size=["2x Large","x Large","Large","Medium","x Mini","2x Mini"]
for item in list_of_size:
    radio_size=Radiobutton(frame_2,text=item,font=("tahoma",12,font.BOLD),variable=x,value=item,anchor=W,bg="#0000ff",fg="#000000")
    radio_size.pack(fill=BOTH,padx=5,pady=3)
# buttun_select=Button(frame_2,text="select",anchor=CENTER,bd=5,font=("tahoma",12,font.BOLD))
# buttun_select.pack(fill=BOTH,expand=True,padx=5,pady=5)
#--------------------------------------------------------select number
label_number=Label(frame_3,text="Number",anchor=CENTER,bd=5,font=("tahoma",12,font.BOLD),bg="#00ff00",fg="#000000")
label_number.pack(fill=BOTH,expand=False,padx=5,pady=2)

slider_number=Scale(frame_3,from_=1,to=10,length=200,tickinterval=1,orient=VERTICAL,bg="#00ff00",fg="#000000")
slider_number.pack(fill=BOTH,padx=5)
# buttun_select=Button(frame_3,text="select",anchor=CENTER,bd=5,font=("tahoma",12,font.BOLD))
# buttun_select.pack(fill=BOTH,expand=True,padx=5,pady=5)
#------------------------------------------------------------------
label_selection=Label(frame_4,text="Orders",font=("tahoma",12,font.BOLD),anchor=CENTER)
label_selection.pack(fill=BOTH)
#------------------------------------------------------------------
# label_foods=Label(frame_4,text="",font=("tahoma",12,font.BOLD),anchor=CENTER)  #روش تابع شماره 8 
# label_foods.pack(fill=BOTH,pady=10)
show_result=Button(frame_4,text="show result",anchor=CENTER,bd=5,pady=4,font=("tahoma",12,font.BOLD),command=func9)
show_result.pack(side=BOTTOM,fill=BOTH,padx=5,pady=5)




root.mainloop()