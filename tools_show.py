# =================================================
# routines to show / plot waves 
# - one wave
# - a line of waves
# - a matrix of waves
# =================================================

import numpy as np
import matplotlib.pyplot as plt

def show_SignalWaveForm (ax, data, title = "", light=False):
    if not (light == False):
        ax.set_ylabel ("ADC counts")
        ax.set_xlabel ("time bin")
    ax.set_xlim (0, 100)
    ax.set_ylim (-32000, 32000)
    if (title != ""):
        ax.set_title (title)
    graph, = ax.plot([], [])
    x_plt = np.linspace (0, len (data), len (data), endpoint=False)
    graph.set_data (x_plt, data)
    plt.draw()

def show_SignalWaveForm_single (data, remark = "", figsize=(5.,4.)):
    fig = plt.figure("SignalWaveForms", figsize=figsize)
    fig.suptitle ("rejected wave")
    ax = fig.subplots (ncols=1, nrows=1, sharex = True, sharey = True)
    show_SignalWaveForm (ax, data, remark)
    plt.show ()

def show_SignalWaveForms (data, title, n_cols=3, n_rows=3, random=False, light=False, figsize=(9.,8.)):
    # --- define a figure
    #if 
    #fig = plt.figure("SignalWaveForms", figsize=(9.,8.))
    fig = plt.figure("SignalWaveForms", figsize=figsize)
    fig.suptitle (title)
    axes = fig.subplots (ncols=n_cols, nrows=n_rows, sharex = True, sharey = True)
    n_data = len (data)
    for col in range (n_cols):
        for row in range (n_rows):
            if random:
                ind = np.random.randint (0, n_data-1)
            else:
                ind = col * n_cols + row
            show_SignalWaveForm (axes [row][col], data [ind]) 