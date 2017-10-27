import numpy as np 
from matplotlib import pyplot as plt

chart_color = ['b', 'b', 'g', 'g', 'r', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k']

def single_line_chart(x_value, y_value, title, style, x_label, y_label):
    
    #plt.subplot(2,1,1)
    
    plt.plot(x_value, y_value, chart_color[0], ls=style, label=title)
    plt.xlabel( x_label, fontsize=10)
    plt.ylabel( y_label, fontsize=10)
    plt.title( 'SysBench CPU POPS BMT', fontsize=20)
    plt.xticks(x_value, rotation=75)
    plt.legend()
    plt.grid()
    plt.savefig( title + 'cpubmt.png')
    plt.show()

def multi_line_chart(values, title, style, x_label, y_label, bmt_title):
    
    filename = 'cpubmt.png'
    
    for i in range(len(values)):
        plt.plot(values[i][0], values[i][1], chart_color[i], ls=style[i], label=title[i], linewidth=1)
        filename = title[i] + filename
    #x = 1.1
    #xscale = [0.00001, 0.0001, 0.001, 0.002, 0.003, 0.005, 0.007, 0.01, 0.02, 0.03, 0.04, 0.05, 0.07, 0.1, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3,0, 5.0, 10.0, 20.0, 30, 50, 100, 150, 256]
    #plt.xticks(xscale)
    #t = np.arange(0.01, 256.0, 0.01)
    #plt.semilogx(t, np.sin(t*2.0))
    plt.xlabel( x_label, fontsize=10)
    plt.ylabel( y_label, fontsize=10)
    plt.title( bmt_title, fontsize=15)
    plt.legend()
    plt.grid(True)
    plt.savefig( filename )
    plt.show()

def bar_chart(data, title, x_label, y_label):
    
    for i in data:
        w = np.arange(len(data[0]))
        plt.bar(w + dist, data[0], color = chart_color[0], width=0.25)
        plt.legend()
        plt.grid()
        plt.text(0, 0, 'Figure. CPU BMT', ha='center')
        plt.savefig('bmt1.png')
        plt.show()

    

def gen_report():
    pass


if __name__ == '__main__':
    pass