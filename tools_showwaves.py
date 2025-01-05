import numpy as np
import matplotlib.pyplot as plt
from general_parameters import LABEL_SIGNAL, LABEL_BACKGROUND, get_label, RANDOM_STATE
    
def show_wave (ax, ind, data, title = "", withLabel=True, withIndex=True, withOrg=True, withContour=True, \
               withAxisLabelling=True, withZeroLine=True):
    ax.set_xlim (0, 100)
    ax.set_ylim (-32000, 32000)
    if withAxisLabelling:
        ax.set_ylabel ("ADC counts")
        ax.set_xlabel ("time bin")

    pic_title = title
    if withIndex:
        index_text = f"wave {ind:d}"
        pic_title = pic_title + index_text
    if withLabel:
        label_text = get_label (data [-1])
        pic_title = pic_title + " " + label_text
    ax.set_title (pic_title)
#        if (title != ""):
#            ax.set_title (title)
    
    if withContour:
        data_con = data [104:129]
        pos_from = data [101]
        graph, = ax.plot ([], [], color='red', linewidth = 2)
        x_plt = np.linspace (0, len (data_con), len (data_con), endpoint=False) + int(pos_from)
        graph.set_data (x_plt, data_con)
        plt.draw()

    if withOrg:
        data_org = data [0:100]
        graph, = ax.plot ([], [], color='blue', linewidth = 1)
        x_plt = np.linspace (0, len (data_org), len (data_org), endpoint=False)
        graph.set_data (x_plt, data_org)
        plt.draw()

    if withZeroLine:
        ax.hlines ([0],[0],[100], colors='green')

def show_waves (data, title = "Signal-Wave-Forms", n_cols=1, n_rows=1, figsize=(5.,4.), source = 'defined', items=[0], \
                withOrg=True, withContour=True, withZeroLine=True, \
                withLabel=True, withIndex=True, withAxisLabelling=False):
    # --- define a figure
    fig = plt.figure(figsize=figsize)
    fig.suptitle (title)
    axes = fig.subplots (ncols=n_cols, nrows=n_rows, sharex = True, sharey = True)

    n_data = len (data)
    ind = 1

    # --- single
    if (n_cols == 1) and (n_rows == 1):
        if (source == "random"):
            ind = np.random.randint (0, n_data-1)
        elif (source == "defined"):
            ind = items [0]
        else:
            ind = 0
        show_wave (axes, ind, data [ind], withLabel=withLabel, withIndex=withIndex, \
                   withOrg=withOrg, withContour=withContour, withAxisLabbeling=withAxisLabelling, withZeroLine=withZeroLine)
        return
    
    # --- line
    if (n_rows == 1):
        for col in range (n_cols):
            if (source == "random"):
                ind = np.random.randint (0, n_data-1)
            elif (source == "defined"):
                ind = items [col]
            else:
                ind = col
            show_wave (axes [col], ind, data [ind], withLabel=withLabel, withIndex=withIndex, \
                       withOrg=withOrg, withContour=withContour, withAxisLabelling=withAxisLabelling, withZeroLine=withZeroLine)
        return

    # --- array
    for col in range (n_cols):
        for row in range (n_rows):
            if (source == "random"):
                ind = np.random.randint (0, n_data-1)
            elif (source == "defined"):
                ind = items [col * n_rows + row]
            else:
                ind = col * n_cols + row

            show_wave (axes [row][col], ind, data [ind], withLabel=withLabel, withIndex=withIndex, \
                       withOrg=withOrg, withContour=withContour, withAxisLabelling=withAxisLabelling, withZeroLine=withZeroLine) 