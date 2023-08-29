import matplotlib.pyplot as plt
import numpy as np

from src._loadingdata import load_data


def drawPlot(data):

    '''max_length = max(len(row) for row in data)
    point_spacing = 0.8
    fig_width = max_length * point_spacing
    fig_height = 6

    plt.figure(figsize=(fig_width, fig_height))
    for i, row in enumerate(data):
        plt.plot(row, label=f'Data Group {i + 1}')

    plt.legend(bbox_to_anchor=(0.95, 1), loc='upper left')
    plt.show()'''



    plt.figure()
    for i, row in enumerate(data):
        plt.plot(row, label=f'Data Group {i + 1}', linewidth=0.3)
    plt.legend(bbox_to_anchor=(0.95, 1), loc='upper left')
    plt.title('_window_width(d): 1000, _overlap(a): 900')
    plt.show()



if __name__ == '__main__':
    '''
    data = load_data("results/_window_width(d): 1000, _overlap(a): 900")
    drawPlot(data)
    '''




    data1 = load_data("results/1)/50, 10%")
    data2 = load_data("results/1)/50, 50%")
    data3 = load_data("results/1)/100, 10%")
    data4 = load_data("results/1)/100, 50%")


    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
    header = ('acc', 'light', 'MVPA', 'sedentary', 'sleep', 'MET')

    for i, row in enumerate(data1):
        ax1.plot(row, label=header[i], linewidth=0.3)
    ax1.set_title('length d = 50, overlap a = 10%')

    for i, row in enumerate(data2):
        ax2.plot(row, label=header[i], linewidth=0.3)
    ax2.set_title('length d = 50, overlap a = 70%')

    for i, row in enumerate(data3):
        ax3.plot(row, label=header[i], linewidth=0.3)
    ax3.set_title('length d = 200, overlap a = 10%')

    for i, row in enumerate(data4):
        ax4.plot(row, label=header[i], linewidth=0.3)
    ax4.set_title('length d = 200, overlap a = 70%')


    #plt.legend(bbox_to_anchor=(0.1, 0.1), loc='upper left')
    fig.set_size_inches(20, 8)
    plt.subplots_adjust(hspace=0.8)
    plt.legend(loc=2, bbox_to_anchor=(1.0, 1.0))
    plt.show()

