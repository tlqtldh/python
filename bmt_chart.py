import numpy as np 
from matplotlib import pyplot as plt

def line_chart(x_value, y_value, title, x_label, y_label):
    
    line_color = ['b', 'r', 'g', 'y']
    #plt.subplot(2,1,1)
    
    plt.plot(x_value, y_value, line_color[0], label=title)
    plt.xlabel( x_label, fontsize=10)
    plt.ylabel( y_label, fontsize=10)
    plt.title('CPU BMT', fontsize=20)
    print(x_value)
    plt.xticks(x_value, rotation=75)
    plt.legend()
    plt.grid()
    plt.text(0, 0, 'Figure. CPU BMT', ha='center')
    plt.savefig('bmt1.png')
    plt.show()

def bar_chart(x, y, title):
    pass

def gen_report():
    pass