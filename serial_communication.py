import serial
import time
import matplotlib.pyplot as plt

arduino = serial.Serial('COM7', 9600)

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
        plt.pause(0.0001)
        k=k+1
        data_to_keep=""
    time.sleep(1)
