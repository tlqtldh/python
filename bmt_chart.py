import numpy as np 
from matplotlib import pyplot as plt

chart_color = ['b', 'r', 'g', 'y']

def single_line_chart(x_value, y_value, title, x_label, y_label):
    
    #plt.subplot(2,1,1)
    
    plt.plot(x_value, y_value, chart_color[0], label=title)
    plt.xlabel( x_label, fontsize=10)
    plt.ylabel( y_label, fontsize=10)
    plt.title( 'CPU BMT', fontsize=20)
    plt.xticks(x_value, rotation=75)
    plt.legend()
    plt.grid()
    plt.text(0, 0, 'Figure. CPU BMT', ha='center')
    plt.savefig('bmt1.png')
    plt.show()

def multi_line_chart(values, title, x_label, y_label):
    
    for i in range(len(values)):
        plt.plot(values[i][0], values[i][1], chart_color[i], label=title[i])
    
    plt.xlabel( x_label, fontsize=10)
    plt.ylabel( y_label, fontsize=10)
    plt.title( 'CPU BMT', fontsize=20)
    plt.legend()
    plt.grid()
    plt.text(0, 0, 'Figure. CPU BMT', ha='center')
    plt.savefig('multi_cpu_bmt.png')
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