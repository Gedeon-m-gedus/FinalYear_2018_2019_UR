
import matplotlib
from numpy import sin, cos, pi
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

import serial
import time

w = numpy.linspace(-2*pi,2*pi,100)
y=4*sin(w)


def my_plot1(a,b,c,d):
    print("I am working properly, you gave me",a," ",b," ",c," ",d)
    x = np.linspace(-50,50,1000)
    y = a*x**3+b*x**2+c*x+d
    plt.plot(x, y, '-r', label='My plot')
    plt.title('Graph of coefficients')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


def my_plot2(a,b,c,d):
    print("I am working properly, you gave me",a," ",b," ",c," ",d)
    x = np.linspace(-50,50,1000)
    y = a*x**3+b*x**2+c*x+d
    plt.plot(x, y, '-r', label='My plot')
    plt.title('Graph of coefficients')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def my_plot3(a,b,c,d):
    print("I am working properly, you gave me",a," ",b," ",c," ",d)
    x = np.linspace(-50,50,1000)
    y = a*x**3+b*x**2+c*x+d
    plt.plot(x, y, '-r', label='My plot')
    plt.title('Graph of coefficients')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def my_plot4(a,b,c,d):
    print("I am working properly, you gave me",a," ",b," ",c," ",d)
    x = np.linspace(-50,50,1000)
    y = a*x**3+b*x**2+c*x+d
    plt.plot(x, y, '-r', label='My plot')
    plt.title('Graph of coefficients')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def my_plot5(a,b,c,d):
    print("I am working properly, you gave me",a," ",b," ",c," ",d)
    x = np.linspace(-50,50,1000)
    y = a*x**3+b*x**2+c*x+d
    plt.plot(x, y, '-r', label='My plot')
    plt.title('Graph of coefficients')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def my_plot6(a,b,c,d):
    print("I am working properly, you gave me",a," ",b," ",c," ",d)
    x = np.linspace(-50,50,1000)
    y = a*x**3+b*x**2+c*x+d
    plt.plot(x, y, '-r', label='My plot')
    plt.title('Graph of coefficients')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def my_plot7(a,b,c,d):
    print("I am working properly, you gave me",a," ",b," ",c," ",d)
    x = np.linspace(-50,50,1000)
    y = a*x**3+b*x**2+c*x+d
    plt.plot(x, y, '-r', label='My plot')
    plt.title('Graph of coefficients')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def my_plot8(a,b,c):
    print("I am working properly, you gave me",a," ",b," ",c)
##    x = np.linspace(-50,50,1000)
##    y = a*x**3+b*x**2+c*x+d
##    plt.plot(x, y, '-r', label='My plot')
##    plt.title('Graph of coefficients')
##    plt.xlabel('x', color='#1C2833')
##    plt.ylabel('y', color='#1C2833')
##    plt.legend(loc='upper left')
##    plt.grid()
##    plt.show()

def my_plot9(a,b,c,d):
    print("I am working properly, you gave me",a," ",b," ",c," ",d)
    x = np.linspace(-50,50,1000)
    y = a*x**3+b*x**2+c*x+d
    plt.plot(x, y, '-r', label='My plot')
    plt.title('Graph of coefficients')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def my_plot10(a,b,c):
    print("I am working properly, you gave me",a," ",b," ",c)
    time=1/b
    time = np.arange(0,90,0.01)
    eq = a*(np.cos((2*np.pi*time)+c))
    plt.plot(time, eq)
    plt.show()
    


    
##
##        plt.title('cosine wave signal')
##        #ax = plt.subplot(111)
##        t = np.arange(0.0, 5.0 , 0.01)
##        s = a*cos(b+c)
##        plt.plot(t,s)
##        #line, = plt.plot(t,s, lw=2)
####        plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
####                     arrowprops=dict(facecolor ='black', shrink=0.05),)
####        plt.annotate('local min', xy=(0.5, -1), xytext=(2, -1.5),
####                     arrowprops=dict(facecolor ='black', shrink=1),)
##
##        plt.ylim(-3 ,3)
##        plt.show()
##kk=my_plot10(10,30,20)
##    x = np.linspace(-50,50,1000)
##    y = a*x**3+b*x**2+c*x+d
##    plt.plot(x, y, '-r', label='My plot')
##    plt.title('Graph of coefficients')
##    plt.xlabel('x', color='#1C2833')
##    plt.ylabel('y', color='#1C2833')
##    plt.legend(loc='upper left')
##    plt.grid()
##    plt.show()

#my_plot(0,0,2,1)
##    legende='sine'
##    title='sine function'
##    plt.plot(angle,fct)
##    plt.ylabel("y")
##    plt.xlabel("x")
##    plt.legend(legende)
##    plt.title(title)
##    plt.show()



def serial_cnft(port):
    arduino = serial.Serial(port, 9600)
    x_cordinates = []
    data_list = []
    data_to_keep=" "
    k=0
    k=int(k)

    while(1):
        data=((arduino.read()).decode("utf-8"))
        print(data)
        data_to_keep=data_to_keep + data
        print(data_to_keep)
        if(data=="$"):
            data_to_keep = data_to_keep.replace('$','')
            data_list.append(float(data_to_keep))
            x_cordinates.append(k)
            print("stored data",data_list[k],"X value",x_cordinates[k])
            #plt.scatter(x_cordinates,temp_list,color='r')
            plt.plot(x_cordinates,data_list,color='r')
            #plt.plot(x_cordinates,turb_list,color='b')
            #labeling x and y axis
            plt.xlabel('Data intries No')
            plt.ylabel('Data values')

            #titlle of my plot
            plt.title('Acquire serial data')
            #to show the graph
            #plt.show()
            plt.pause(0.0000001)
            k=k+1
            data_to_keep=""
        #time.sleep(1)
    #____________________________
