"""
A collection of  graphing  functions for outlier detection/graphing
of fd, dvars, and meanSignal
"""
import numpy as np
import matplotlib.pyplot as plt

# Calculate mean this is same as the one in basic_util.py 
# Test already written, included here because graphing functions not tested
# but need to use above: 
def vol_mean(data):
    """ Return mean across voxels for $D `data`
    
    Input:
        np array of data
    Output: np array of dim (T,)
        mean of data across all but the last dimension
    """
    mean_list = []
    # Loop over the each volume and outputs the mean of each dimension
    for i in range(data.shape[-1]):
        mean = np.mean(data[...,i])
        mean_list.append(mean)
    return np.asarray(mean_list)


# Graphing dvars: RMS signal derivative    
def plot_dvars(dvars_dict, dvars_outliers, saveit=False):
    """
    Input:
        Dictionary of dvars_dict: {name of output file: data}
        dvars_outliers: A list of outliers
        Saveit: boolean that indicates whether user wants to save the plot
    Output:
        Plot of dvars by timepoints
        Boundlines indicate potential points of outliers
    """
    # boundary should be set to 0.3-0.5
    bound = np.array([0.5]*(240))
    # making x axis values for outliers
    x = np.arange(len(dvars_dict.values()[0]))
    # plotting
    fig = plt.figure(figsize=(10,4))
    ax = fig.add_subplot(111)
    plt.xlim(0,240)
    # plt.ylim(-0.05, 1.0)
    ax.plot(dvars_dict.values()[0])
    ax.scatter(x[dvars_outliers], dvars_dict.values()[0][dvars_outliers], marker='o', color='r')
    ax.plot(bound, 'g--')
    plt.ylabel('DVARS')
    plt.xlabel('timepoints')
    plt.title('DVARS (RMS Signal Derivative over brain mask)')
    if saveit:
        plt.savefig(dvars_dict.keys()[0])
        plt.close()


# Graphing fd: Framewise displacement
def plot_fd(fd_dict, fd_outliers, saveit=False):
    """
    Input:
        Dictionary of fd_dict: {name of output file: data}
        fd_outliers: A list of fd outliers
        Saveit: boolean that indicates whether user wants to save the plot
    Output:
        Plot of fd(framewise displacement) by timepoints
        Boundline indicate potential points of outliers
    """
    # boundary should be set to 0.2-0.5
    bound = np.array([0.5]*(240))
    # making x axis values for outliers
    x = np.arange(len(fd_dict.values()[0]))
    # plotting
    fig = plt.figure(figsize=(10,4))
    ax = fig.add_subplot(111)
    plt.xlim(0,240)    
    # plt.ylim(0, 0.6)
    ax.plot(fd_dict.values()[0])
    ax.scatter(x[fd_outliers], fd_dict.values()[0][fd_outliers], marker='o', color='r')
    ax.plot(bound, 'g--')
    plt.ylabel('FD')
    plt.xlabel('timepoints')
    plt.title('Framewise Displacement')
    if saveit:
        plt.savefig(fd_dict.keys()[0])
        plt.close()


# Graphing mean signal	
def plot_meanSig(bdata_dict, saveit = False):
    """
    Input:
        Dictionary of bold data with the _dict: {name of output file: data}
        Saveit: boolean that indicates whether user wants to save the plot
    Output:
        Plot of mean signal  by timepoints
        Fitted polynomial curve
    """
    data = bdata_dict.values()[0]
    x = list(range(data.shape[-1]))
    y = vol_mean(data)
    # fit a quadratic function for mean signal data
    coefficients = np.polyfit(x, y, 2)
    polynomial = np.poly1d(coefficients)
    xs = np.arange(1, data.shape[-1], 1)
    ys = polynomial(xs)
    # plot
    fig = plt.figure(figsize=(10,4))
    ax = fig.add_subplot(111)
    plt.xlim(0,data.shape[-1])
    ax.plot(x, y)
    ax.plot(xs, ys)
    plt.ylabel('Mean MR signal')
    plt.xlabel('timepoints')
    plt.title('Mean signal (unfiltered)')
    if saveit:
        plt.savefig(bdata_dict.keys()[0])
        plt.close()

