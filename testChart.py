from datetime import datetime, date
import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
import pathlib

# Define dataset
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 2, 3, 4, 5, 8, 8, 9, 3, 1])


def create_visualization(x, y):
    '''
      Create Visualization
      return:
        - saves the created plot in ./results/
        - dir: path to working directory
        - path: path to saved plot
    '''

    # Font size
    plt.rc('font', size=22)
    plt.rc('axes', titlesize=22)
    plt.rc('axes', labelsize=20)
    plt.rc('xtick', labelsize=18)
    plt.rc('ytick', labelsize=18)
    plt.rc('legend', fontsize=18)
    plt.rc('figure', titlesize=22)

    # Create new plot with matplotlib
    # fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(14, 7))
    fig, ax = plt.subplots(figsize=(14, 7))

    # Add a bar plot to the figure
    ax.bar(x, y, color='grey')
    ax.set(xlabel="Day", ylabel="Hours [h]")
    # plt.xlabel("Day")
    # plt.ylabel("Day")

    # Define filename with current date e.g. "2021-04-08.png"
    filename = str(date.today()) + ".png"

    # Working directory
    dir = pathlib.Path(__file__).parent.absolute()

    # Folder where the plots should be saved
    folder = r"/results/"

    path_plot = str(dir) + folder + filename

    # Save the plot
    fig.savefig(path_plot, dpi=200)

    return path_plot, dir


path_plot, dir = create_visualization(x, y)
