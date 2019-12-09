
#used modules
import tkinter #gui module
import pyautogui #screenshot
import time
import uuid #random string generator

#_________MATH AND PLOT LIBRAY__________
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation



import numpy
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot  
import matplotlib.animation as animation


from tkinter import *
from tkinter import messagebox as tkMessageBox

#_____________OUR DEFINED LIBRARY__________________________

import garelly_functions
import control_functions
import user_defined_functions



myapp = tkinter.Tk()#naming my App
myapp.geometry("700x500+0+0")#setting the size of my App
myapp.resizable(0,0) #disabling the maximize button
sbmyapp = Scrollbar(myapp)  #scroll bar of my App
sbmyapp.pack(side = RIGHT, fill = Y)


#__________APP FRAMES_____________________________________
#__________top frame______________________________________
top_frame=Frame(myapp,width = 700,height=50,bg="gray64",relief=SUNKEN)
top_frame.pack(side=TOP)
app_tittle = Label(top_frame,font=('arial',20,'bold'),text="SIGNAL AND FUNCTION ANALYZER",fg="darkblue",bd=10)
app_tittle.grid(row=0,column=0)

#__________user frame_____________________________________
user_frame=Frame(myapp,width = 480,height=300,bg="gray64",relief=SUNKEN)
user_frame.pack(side=RIGHT)
#__________user frame header______________________________
user_frame_header = tkinter.Canvas(myapp, bg="gray64", height=25, width=250,cursor='dot')
user_frame_header.create_text(90,15,fill="darkblue",font="Times 10 italic bold",text="WORK SPACE")
user_frame_header.pack()
user_frame_header.place(x=200, y=90)
#___________user input path_______________________
user_frame_header_insert_equation = tkinter.Canvas(myapp, bg="gray64", height=25, width=160,cursor='dot')
user_frame_header_insert_equation.create_text(90,15,fill="darkblue",font="Times 10 italic bold",text="INSERT EQUATION")
user_frame_header_insert_equation.pack()
user_frame_header_insert_equation.place(x=520, y=90)
#__________user input fanctions frame__________________________________
user_input_function_frame=Frame(user_frame,width =158,height=100,bg="white",relief=SUNKEN)
#sbgarely = Scrollbar(user_input_function_frame)
#sbgarely.pack(side = RIGHT, fill = Y)
user_input_function_frame.pack()
user_input_function_frame.place(x=318,y=0)
mylist1 = Listbox(user_input_function_frame,fg="red",bg="white",width = 26,height=10 )
mylist1.insert(1, ">> Quadratic equation")
mylist1.insert(2, ">> EMW eaquations")
mylist1.insert(3, ">> Exponential equation")
mylist1.insert(4, ">> Pulse plotting")
mylist1.insert(5, ">> Transfer function")
mylist1.insert(6, ">> Diode equation")
mylist1.insert(7, ">> Three phase function")
mylist1.insert(8, ">> Sine function")
mylist1.insert(9, ">> Cosine vs sine function")
mylist1.insert(10, ">> Cosine function")

mylist1.pack( side = RIGHT )  

#__________garelly frame__________________________________
garelly_frame=Frame(myapp,width = 250,height=400,bg="white",relief=SUNKEN)
sbgarely = Scrollbar(garelly_frame)
sbgarely.pack(side = RIGHT, fill = Y)
garelly_frame.pack(side=LEFT)
#__________garelly frame header___________________________
garelly_frame_header = tkinter.Canvas(myapp, bg="gray64", height=25, width=180,cursor='dot')
garelly_frame_header.create_text(90,15,fill="darkblue",font="Times 10 italic bold",text="BUILT IN FUNCTIONS")
garelly_frame_header.pack()
garelly_frame_header.place(x=0, y=90)

#_______function list with in garelly frame_______________
mylist = Listbox(garelly_frame, yscrollcommand = sbgarely.set,fg="blue",width = 30,height=18,font="Aerial 10" )
mylist.insert(1, ">> Oscillation decay")
mylist.insert(2, ">> Dumping oscillation")
mylist.insert(3, ">> EMW propagation")
mylist.insert(4, ">> Pulse generation")
mylist.insert(5, ">> Time responce analysis")
mylist.insert(6, ">> Time domain specifications")
mylist.insert(7, ">> System stability")
mylist.insert(8, ">> Root locus")
mylist.insert(9, ">> Sine wave")
mylist.insert(10,">> Cosine wave")
mylist.insert(11,">> Affine function")
mylist.insert(12,">> Diode V-I characteristic")
mylist.insert(13,">> Three phase voltages")
mylist.insert(14,">> Three phase current")
mylist.insert(15,">> Ohms low curve")
mylist.insert(16,">> Step responce")
mylist.insert(17,">> Impulse responce")
mylist.insert(18,">> Open and Closed bode plot")
mylist.insert(19,">> Sinc function")
mylist.insert(20,">> Distrubution function")
mylist.insert(21,">> Area under curve")

mylist.pack( side = LEFT )  
sbgarely.config( command = mylist.yview )  


#_________READ SETIAL DATA__________________
def read_serial_data():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button
        
        k.title("Acquire Serial Data")
        

        def get_seial_info():
            global com_port
            global com_speed
            global com_port_full_data
            
      
            com_port= com_port_entryy.get()
            com_speed= com_speed_entryy.get()
            
            print("port  ", com_port)
            com_port_full_data='COM'+com_port
            print(com_port_full_data)
            print("Speed  ", com_speed)
            
            user_defined_functions.serial_cnft(com_port_full_data)

        com_port_entryy=Entry(k)
        com_speed_entryy=Entry(k)
        

        com_port_label=Label(k,text="Enter COM Port   ")
        com_speed_label=Label(k,text="Enter Frequency ")
        
        
        com_port_label.place(x=10, y=35)
        com_speed_label.place(x=10, y=60)
        
                
        com_port_entryy.place(x=125, y=35)
        com_speed_entryy.place(x=125, y=60)
        t=tkinter.Button(k, text="GET DATA",font="Times 10 italic bold",fg="black",bg="yellow",command=get_seial_info)
        t.pack()
        t.place(x=120, y=235)
      



#__________MENU BAR CLASS & FUNCTIONS________________
class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("FEEL SCIENTIST")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)


        #this commands help to use menu
        menu=Menu(self.master)
        self.master.config(menu=menu)


        #these that follows are for file
        file=Menu(menu)
        file.add_command(label='New')
        file.add_command(label='Open')
        file.add_command(label='Recents')
        file.add_command(label='Examples')
        file.add_command(label='Capture screen       ',command=control_functions.screenshoot)
        file.add_separator()
        file.add_command(label='Quit',command=control_functions.quitfunction)



        #for the edit portal
        edit=Menu(menu)
        edit.add_command(label='Undo ')
        edit.add_command(label='Fonts               ')

         #for the library portal
        library=Menu(menu)
        library.add_command(label='Add library ')
        library.add_command(label='Remove library     ')
        #library.add_command(label='Acquire Serial signal')

        #for serial data com
        serial=Menu(menu)
        serial.add_command(label='Acquire Serial signal',command=read_serial_data)

        #for the help portal
        Help=Menu(menu)
        Help.add_command(label='Open help text   ')



        #these are for the portal in the menu
        menu.add_cascade(label='File',menu=file)
        menu.add_cascade(label='Edit',menu=edit)
        menu.add_cascade(label='Library',menu=library)
        menu.add_cascade(label='Serial',menu=serial)
        menu.add_cascade(label='Help',menu=Help)

#__________calling the menu class___________
menu_of_myapp = Window(myapp)



def userSelection():
    Selected_function=mylist.curselection()
    b='0'
   
   
    for i in Selected_function:
        b=mylist.get(i)
        print(b)
##    if b=="0":
##        tkMessageBox.showinfo( "Hello user", "Please select built in function you want")
    if b==">> Dumping oscillation":
       f1=garelly_functions.dumping_oscillation()
    if b==">> Pulse generation":
       f1=garelly_functions.pulse_generation()
    if b==">> Sine wave":
       f1=garelly_functions.sine_wave()
    if b==">> Cosine wave":
       f1=garelly_functions.cosine_wave()
    if b==">> Three phase voltages":
       f1=garelly_functions.three_phase_wave()
    if b==">> Three phase current":
       f1=garelly_functions.three_phase_wave()
    if b==">> Sinc function":
       f1=garelly_functions.sinc_function()
    if b==">> Distrubution function":
       f1=garelly_functions.distrubution_function()
    if b==">> Area under curve":
       f1=garelly_functions.area_area_under_curve()
    if b==">> Oscillation decay":
       f1=garelly_functions.oscillation_decay()

#___________FUNCTION FOR LINKING BUTTON AND SELECTED SIGNAL IN INSERT __________

def userSelection1():
    prefered_function=mylist1.curselection()
    bb='0'

 
    for k in prefered_function:
        bb=mylist1.get(k)
        print(bb)
##    if bb=="0":
##        tkMessageBox.showinfo( "Hello user", "Please select function format you want")
    if bb==">> Quadratic equation":
        f2=Top_Levels_user_input.toplevelwindow1()
    if bb==">> EMW eaquations":
        f2=Top_Levels_user_input.toplevelwindow2()
    if bb==">> Exponential equation":
        f2=Top_Levels_user_input.toplevelwindow3()
    if bb==">> Pulse plotting":
        f2=Top_Levels_user_input.toplevelwindow4()
    if bb==">> Transfer function":
        f2=Top_Levels_user_input.toplevelwindow5()
    if bb==">> Diode equation":
        f2=Top_Levels_user_input.toplevelwindow6()
    if bb==">> Three phase function":
        f2=Top_Levels_user_input.toplevelwindow7()
    if bb==">> Sine function":
        f2=Top_Levels_user_input.toplevelwindow8()
    if bb==">> Cosine vs sine function":
        f2=Top_Levels_user_input.toplevelwindow9()
    if bb==">> Cosine function":
        f2=Top_Levels_user_input.toplevelwindow10()

class Top_Levels_user_input:
    
    def toplevelwindow1():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button
        k.title("Quadratic equation")

##        CheckVar1 = IntVar()
##        CheckVar2 = IntVar()
        
        #__________FUNCTION TO GET USER INPUT DATA_________
        def data_for_quadratic_eq():
            global a
            global b
            global c
            global d
      
            a= a_entryy.get()
            b= b_entryy.get()
            c= c_entryy.get()
            d= d_entryy.get()
            
            print("data 1 "+a)
            print("data 2 "+b)
            print("data 3 "+c)
            print("data 4 "+d)
            
            a=float(a)
            b=float(b)
            c=float(c)
            d=float(d)
            
            print("data  ", a)
            print("data  ", b)
            print("data  ", c)
            print("data  ", d)
            user_defined_functions.my_plot1(a,b,c,d)

        a_entryy=Entry(k)
        b_entryy=Entry(k)
        c_entryy=Entry(k)
        d_entryy=Entry(k)

        a_label=Label(k,text="First coefficient  a   ")
        b_label=Label(k,text="Second coefficient b")
        c_label=Label(k,text="Third coeffient    c   ")
        d_label=Label(k,text="Fourth coeffient    d")
        
        a_label.place(x=10, y=35)
        b_label.place(x=10, y=60)
        c_label.place(x=10, y=85)
        d_label.place(x=10, y=110)
                
        a_entryy.place(x=125, y=35)
        b_entryy.place(x=125, y=60)
        c_entryy.place(x=125, y=85)
        d_entryy.place(x=125, y=110)


##        C1 = Checkbutton(k, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20).pack()
##        C2 = Checkbutton(k, text = "Music", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20).pack()
##        C1.place(x=120, y=5)
##        C2.place(x=150, y=5)


        t=tkinter.Button(k, text="   PLOT    ",font="Times 10 italic bold",fg="black",bg="green",command=data_for_quadratic_eq)
        t.pack()
        t.place(x=120, y=235)
        
##        sleep(10)
##
##        while(a_entryy.get() == "" or a_entryy.get() == "0"):
##            a= a_entryy.get()
##            print("inside a:" + a)
##        while(b_entryy.get()== "" or b_entryy.get() == "0"):
##            b= b_entryy.get()
##            print("inside b:" + b)
##        while(c_entryy.get()== "" or c_entryy.get() == "0"):
##            c= c_entryy.get()
##            print("inside c:" + c)
##        while(d_entryy.get()== "" or d_entryy.get() == "0"):
##            d= d_entryy.get()
##            print("inside d:" + d)
##        
##        #____GETTING DATA FROM ENTRY IN THE USER DEFINED FUNCTIONS_____________-
##

        
##
##        print("data 1 "+a)
##        print("data 2 "+b)
##        print("data 3 "+c)
##        print("data 4 "+d)

        
    def toplevelwindow2():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button
        k.title("EMW eaquations")
        t=tkinter.Button(k, text="   PLOT    ",font="Times 10 italic bold",fg="black",bg="yellow",command=userSelection)
        t.pack()
        t.place(x=120, y=235)
        
    def toplevelwindow3():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button
        k.title("Exponential equation")
        
        a_entryy=Entry(k)
        b_entryy=Entry(k)
        c_entryy=Entry(k)
        
        a_label=Label(k,text="Amplitude")
        b_label=Label(k,text="Angle")
        c_label=Label(k,text="Phase")
        
        a_label.place(x=10, y=35)
        b_label.place(x=10, y=60)
        c_label.place(x=10, y=85)
      
        
        a_entryy.place(x=125, y=35)
        b_entryy.place(x=125, y=60)
        c_entryy.place(x=125, y=85)
        
        t=tkinter.Button(k, text="   PLOT    ",font="Times 10 italic bold",fg="black",bg="yellow",command=userSelection)
        t.pack()
        t.place(x=120, y=235)
        
    def toplevelwindow4():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button
        k.title("Pulse plotting")

        a_entryy=Entry(k)
        b_entryy=Entry(k)
 
        a_label=Label(k,text="Pulse dulation")
        b_label=Label(k,text="Pulse Amplitude")
        
        a_label.place(x=10, y=35)
        b_label.place(x=10, y=60)
        
        a_entryy.place(x=125, y=35)
        b_entryy.place(x=125, y=60)
        
        t=tkinter.Button(k, text="   PLOT    ",font="Times 10 italic bold",fg="black",bg="yellow",command=userSelection)
        t.pack()
        t.place(x=120, y=235)
        
    def toplevelwindow5():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button
        t=tkinter.Button(k, text="   PLOT    ",font="Times 10 italic bold",fg="black",bg="yellow",command=userSelection)
        t.pack()
        t.place(x=120, y=235)

    def toplevelwindow6():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button
        t=tkinter.Button(k, text="   PLOT    ",font="Times 10 italic bold",fg="black",bg="yellow",command=userSelection)
        t.pack()
        t.place(x=120, y=235)

    def toplevelwindow7():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button
        t=tkinter.Button(k, text="   PLOT    ",font="Times 10 italic bold",fg="black",bg="yellow",command=userSelection)
        t.pack()
        t.place(x=120, y=235)
    def toplevelwindow8():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button
        k.title("Sine function")
                #__________FUNCTION TO GET USER INPUT DATA_________
        def data_for_sine_eq():
            global a
            global b
            global c
            #global d
      
            a= a_entryy.get()
            b= b_entryy.get()
            c= c_entryy.get()
            #d= d_entryy.get()
            
            print("data 1 "+a)
            print("data 2 "+b)
            print("data 3 "+c)
            #print("data 4 "+d)
            
            a=float(a)
            b=float(b)
            c=float(c)
            #d=float(d)
            
            print("data  ", a)
            print("data  ", b)
            print("data  ", c)
            #print("data  ", d)
            user_defined_functions.my_plot8(a,b,c)

        a_entryy=Entry(k)
        b_entryy=Entry(k)
        c_entryy=Entry(k)
        
        a_label=Label(k,text="Amplitude")
        b_label=Label(k,text="Angle")
        c_label=Label(k,text="Phase")
      
        a_label.place(x=10, y=35)
        b_label.place(x=10, y=60)
        c_label.place(x=10, y=85)
      
        a_entryy.place(x=125, y=35)
        b_entryy.place(x=125, y=60)
        c_entryy.place(x=125, y=85)
      
        t=tkinter.Button(k, text="   PLOT    ",font="Times 10 italic bold",fg="black",bg="yellow",command=data_for_sine_eq)
        t.pack()
        t.place(x=120, y=235)
        
    def toplevelwindow9():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button

        a_entryy=Entry(k, width=10)
        b_entryy=Entry(k, width=10)
        c_entryy=Entry(k, width=10)

        a_entryy2=Entry(k, width=10)
        b_entryy2=Entry(k, width=10)
        c_entryy2=Entry(k, width=10)
        
        a_label=Label(k,text="Amplitude")
        b_label=Label(k,text="Angle")
        c_label=Label(k,text="Phase")

        sine_label=Label(k,text="     Sine      ")
        cosine_label=Label(k,text="   Cosine   ")
      
        a_label.place(x=10, y=35)
        b_label.place(x=10, y=60)
        c_label.place(x=10, y=85)

        sine_label.place(x=75, y=10)
        cosine_label.place(x=145, y=10)
      
        a_entryy.place(x=75, y=35)
        b_entryy.place(x=75, y=60)
        c_entryy.place(x=75, y=85)

        a_entryy2.place(x=145, y=35)
        b_entryy2.place(x=145, y=60)
        c_entryy2.place(x=145, y=85)
 
        t=tkinter.Button(k, text="   PLOT    ",font="Times 10 italic bold",fg="black",bg="yellow",command=userSelection)
        t.pack()
        t.place(x=120, y=235)
        
    def toplevelwindow10():
        k=Toplevel(bg="gray64")
        k.geometry("310x265+207+180")#setting the size of my App
        k.resizable(0,0) #disabling the maximize button
        k.title("Cosine function")
        
        #__________FUNCTION TO GET USER INPUT DATA_________
        def data_for_cosine_eq():
            global a
            global b
            global c
            #global d
      
            a= a_entryy.get()
            b= b_entryy.get()
            c= c_entryy.get()
            #d= d_entryy.get()
            
            print("data 1 "+a)
            print("data 2 "+b)
            print("data 3 "+c)
            #print("data 4 "+d)
            
            a=float(a)
            b=float(b)
            c=float(c)
            #d=float(d)
            
            print("data  ", a)
            print("data  ", b)
            print("data  ", c)
            #print("data  ", d)
            user_defined_functions.my_plot10(a,b,c)

        a_entryy=Entry(k)
        b_entryy=Entry(k)
        c_entryy=Entry(k)
   
        a_label=Label(k,text="Amplitude")
        b_label=Label(k,text="Frequency")
        c_label=Label(k,text="Phase")
      
        a_label.place(x=10, y=35)
        b_label.place(x=10, y=60)
        c_label.place(x=10, y=85)    
        a_entryy.place(x=125, y=35)
        b_entryy.place(x=125, y=60)
        c_entryy.place(x=125, y=85)
      
        t=tkinter.Button(k, text="   PLOT    ",font="Times 10 italic bold",fg="black",bg="blue",command=data_for_cosine_eq)
        t.pack()
        t.place(x=120, y=235)




#______ BUTTONS FOR INPUTING FUNCTIONS______


#buttons'name and their commands
plot_button=tkinter.Button(user_frame, text="   PLOT    ",font="Times 15 italic bold",fg="black",bg="yellow",command=userSelection)
clear_button=tkinter.Button(user_frame, text="  CLEAR  ",font="Times 15 italic bold",fg="black",bg="red")
insert_button=tkinter.Button(user_frame, text="                  Insert                    ",font="Times 10 italic bold",fg="black",bg="red",command=userSelection1)


#packing buttons
plot_button.pack()
clear_button.pack()
insert_button.pack()


#locating buttons
plot_button.place(x=5, y=255)
clear_button.place(x=120, y=255)
insert_button.place(x=320, y=163)



#____________THE ROOTS______________________

myapp.mainloop()


