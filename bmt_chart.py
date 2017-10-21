import numpy as np 
from matplotlib import pyplot as plt

chart_color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k']

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

def multi_line_chart(values, title, style, x_label, y_label):
    
    filename = 'cpubmt.png'
    
    for i in range(len(values)):
        plt.plot(values[i][0], values[i][1], chart_color[i], ls=style[i], label=title[i])
        filename = title[i] + filename
    
    plt.xlabel( x_label, fontsize=10)
    plt.ylabel( y_label, fontsize=10)
    plt.title( 'LMBench Memory Latency BMT', fontsize=20)
    plt.legend()
    plt.grid()
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