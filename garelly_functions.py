#_________MATH AND PLOT LIBRAY__________
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation


import numpy
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot  
import matplotlib.animation as animation

#_______________________________________
#______________CLASS GARELLY OF FUNCTIONS PLOT_____________

##############################_______OSCILLATION DECAY_______#############################################
def dumping_oscillation():
        def data_gen(t=0):
            cnt = 0
            while cnt < 1000:
                cnt += 1
                t += 0.1
                yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)


        def init():
            ax.set_ylim(-1.1, 1.1)
            ax.set_xlim(0, 10)
            del xdata[:]
            del ydata[:]
            line.set_data(xdata, ydata)
            return line,

        fig, ax = plt.subplots()
        line, = ax.plot([], [], lw=2)
        ax.grid()
        xdata, ydata = [], []


        def run(data):
            # update the data
            t, y = data
            xdata.append(t)
            ydata.append(y)
            xmin, xmax = ax.get_xlim()

            if t >= xmax:
                ax.set_xlim(xmin, 2*xmax)
                ax.figure.canvas.draw()
            line.set_data(xdata, ydata)

            return line,
        plt.title('dumping oscillation')

        ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                                      repeat=False, init_func=init)
        plt.show()


#################################___PULSE GENERATION_____#################################################
def pulse_generation():
    class Scope(object):
        def __init__(self, ax, maxt=2, dt=0.02):
            self.ax = ax
            self.dt = dt
            self.maxt = maxt
            self.tdata = [0]
            self.ydata = [0]
            self.line = Line2D(self.tdata, self.ydata)
            self.ax.add_line(self.line)
            self.ax.set_ylim(-.1, 1.1)
            self.ax.set_xlim(0, self.maxt)

        def update(self, y):
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  # reset the arrays
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + self.dt
            self.tdata.append(t)
            self.ydata.append(y)
            self.line.set_data(self.tdata, self.ydata)
            return self.line,


    def emitter(p=0.03):
        'return a random value with probability p, else 0'
        while True:
            v = np.random.rand(1)
            if v > p:
                yield 0.
            else:
                yield np.random.rand(1)

    # Fixing random state for reproducibility
    np.random.seed(19680801)


    fig, ax = plt.subplots()
    scope = Scope(ax)

    # pass a generator in "emitter" to produce data for the update func
    ani = animation.FuncAnimation(fig, scope.update, emitter, interval=10,
                                  blit=True)

    plt.show()

###############################_______COSINE WAVE ______________##############################################################3

def cosine_wave():
        plt.title('cosine wave signal')
        ax = plt.subplot(111)
        t = np.arange(0.0, 5.0 , 0.01)
        s = np.cos(2*np.pi*t)
        line, = plt.plot(t,s, lw=2)
        plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                     arrowprops=dict(facecolor ='black', shrink=0.05),)
        plt.annotate('local min', xy=(0.5, -1), xytext=(2, -1.5),
                     arrowprops=dict(facecolor ='black', shrink=1),)

        plt.ylim(-3 ,3)
        plt.show()
#k=  cosine_wave()       

################################________SINE WAVE ______________########################################
def sine_wave():
        plt.title('sine wave signal')
        ax = plt.subplot(111)
        t = np.arange(0.0, 5.0 , 0.01)
        s = np.sin(2*np.pi*t)
        line, = plt.plot(t,s, lw=2)
        plt.annotate('local max', xy=(2.25, 1), xytext=(3, 1.5),
                     arrowprops=dict(facecolor ='black', shrink=0.05),)
        plt.annotate('local min', xy=(0.75, -1), xytext=(2, -1.5),
                     arrowprops=dict(facecolor ='black', shrink=1),)

        plt.ylim(-3 ,3)
        plt.show()
#k=  sine_wave() 

#############################___THREE PHASE SIGNAL_________#############################################
def three_phase_wave():
        plt.title('three phase signal')

        ax = plt.subplot(111)
        t = np.arange(0.0, 5.0 , 0.01)
        s = np.sin(2*np.pi*t)
        ss = np.sin(2*np.pi*t+120)
        sss = np.sin(2*np.pi*t+240)
        line, = plt.plot(t,s, lw=2)
        line, = plt.plot(t,ss, lw=2)
        line, = plt.plot(t,sss, lw=2)
        plt.ylim(-3 ,3)
        plt.show()
#k=three_phase_wave()

###############################____second order equations_____#############################################
def second_order():
        a=int(input("first coeficient"))
        b=int(input("second coeficient"))
        c=int(input("constant"))
        x = np.linspace(-20,20,20)
        y = a*x**2 + b*x + c
        #plt.ylim(-3 ,3)
        plt.plot(x,y)
        plt.show()
#k=second_order()
########################______sinc_function__________#################################################
def sinc_function():
        X = np.linspace(-6,6, 1024)
        Y = np.sinc(X)
        plt.title('sinc_function') # a little notation
        plt.xlabel('array variables') #adding xlabel
        plt.ylabel('random variables') #adding ylabel
        #plt.text(-5, 0.4, 'Matplotlib') # -5 is the x value and 0.4 is y value
        plt.plot(X,Y, color='r', marker ='o',markersize =3,markevery = 30, markerfacecolor='w',linewidth= 3.0,markeredgecolor = 'b')
        plt.show()

######################____distribution function______#################
def distrubution_function():
        def gf(X, mu, sigma):
            a = 1. /(sigma*np.sqrt(2. * np.pi))
            b = -1. /(2. * sigma **2)
            return a * np.exp(b * (X - mu)**2)

        X = np.linspace(-6, 6, 1024)
        for i in range(64):
            samples = np.random.standard_normal(50)
            mu,sigma = np.mean(samples), np.std(samples)
            plt.plot(X, gf(X, mu, sigma),color = '.75',linewidth='.5')

        plt.plot(X,gf(X, 0., 1.),color ='.00',linewidth=3.)
        plt.show()

##########################_____integral finding area under the curve_____########
def area_area_under_curve():
        def func(x):
            return (x - 3) * (x - 5) * (x - 7) + 85


        a, b = 2, 9  # integral limits
        x = np.linspace(0, 10)
        y = func(x)

        fig, ax = plt.subplots()
        plt.plot(x, y, 'r', linewidth=2)
        plt.ylim(ymin=0)

        # Make the shaded region
        ix = np.linspace(a, b)
        iy = func(ix)
        verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
        poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
        ax.add_patch(poly)

        plt.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
                 horizontalalignment='center', fontsize=20)

        plt.figtext(0.9, 0.05, '$x$')
        plt.figtext(0.1, 0.9, '$y$')

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.xaxis.set_ticks_position('bottom')

        ax.set_xticks((a, b))
        ax.set_xticklabels(('$a$', '$b$'))
        ax.set_yticks([])

        plt.show()

#################################____oscillationdecay___################################################
def oscillation_decay():
        # Sent for figure
        font = {'size'   : 9}
        matplotlib.rc('font', **font)

        # Setup figure and subplots
        f0 = figure(num = 0, figsize = (12, 8))#, dpi = 100)
        f0.suptitle("Oscillation decay", fontsize=12)
        ax01 = subplot2grid((2, 2), (0, 0))
        ax02 = subplot2grid((2, 2), (0, 1))
        ax03 = subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
        ax04 = ax03.twinx()
        #tight_layout()

        # Set titles of subplots
        ax01.set_title('Position vs Time')
        ax02.set_title('Velocity vs Time')
        ax03.set_title('Position and Velocity vs Time')

        # set y-limits
        ax01.set_ylim(0,2)
        ax02.set_ylim(-6,6)
        ax03.set_ylim(-0,5)
        ax04.set_ylim(-10,10)

        # set x-limits
        ax01.set_xlim(0,5.0)
        ax02.set_xlim(0,5.0)
        ax03.set_xlim(0,5.0)
        ax04.set_xlim(0,5.0)

        # Turn on grids
        ax01.grid(True)
        ax02.grid(True)
        ax03.grid(True) 

        # set label names
        ax01.set_xlabel("x")
        ax01.set_ylabel("py")
        ax02.set_xlabel("t")
        ax02.set_ylabel("vy")
        ax03.set_xlabel("t")
        ax03.set_ylabel("py")
        ax04.set_ylabel("vy")

        # Data Placeholders
        yp1=zeros(0)
        yv1=zeros(0)
        yp2=zeros(0)
        yv2=zeros(0)
        t=zeros(0)

        # set plots
        p011, = ax01.plot(t,yp1,'b-', label="yp1")
        p012, = ax01.plot(t,yp2,'g-', label="yp2")  

        p021, = ax02.plot(t,yv1,'b-', label="yv1")
        p022, = ax02.plot(t,yv2,'g-', label="yv2")

        p031, = ax03.plot(t,yp1,'b-', label="yp1")
        p032, = ax04.plot(t,yv1,'g-', label="yv1")

        # set lagends
        ax01.legend([p011,p012], [p011.get_label(),p012.get_label()])
        ax02.legend([p021,p022], [p021.get_label(),p022.get_label()])
        ax03.legend([p031,p032], [p031.get_label(),p032.get_label()])

        # Data Update
        xmin = 0.0
        xmax = 5.0
        x = 0.0

        def updateData(self):
                global x
                global yp1
                global yv1
                global yp2
                global yv2
                global t

                tmpp1 = 1 + exp(-x) *sin(2 * pi * x)
                tmpv1 = - exp(-x) * sin(2 * pi * x) + exp(-x) * cos(2 * pi * x) * 2 * pi
                yp1=append(yp1,tmpp1)
                yv1=append(yv1,tmpv1)
                yp2=append(yp2,0.5*tmpp1)
                yv2=append(yv2,0.5*tmpv1)
                t=append(t,x)

                x += 0.05

                p011.set_data(t,yp1)
                p012.set_data(t,yp2)

                p021.set_data(t,yv1)
                p022.set_data(t,yv2)

                p031.set_data(t,yp1)
                p032.set_data(t,yv1)

                if x >= xmax-1.00:
                        p011.axes.set_xlim(x-xmax+1.0,x+1.0)
                        p021.axes.set_xlim(x-xmax+1.0,x+1.0)
                        p031.axes.set_xlim(x-xmax+1.0,x+1.0)
                        p032.axes.set_xlim(x-xmax+1.0,x+1.0)

                return p011, p012, p021, p022, p031, p032

        # interval: draw new frame every 'interval' ms
        # frames: number of frames to draw
        simulation = animation.FuncAnimation(f0, updateData, blit=False, frames=200, interval=20, repeat=False)

        # Uncomment the next line if you want to save the animation
        #simulation.save(filename='sim.mp4',fps=30,dpi=300)

        plt.show()

