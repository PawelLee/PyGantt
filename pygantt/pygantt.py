# -*- coding: utf-8 -*-

"""Main module."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def gantt(task=None, start=None, finish=None, **kwargs):
    """ Plot a gantt chart.
    """

    if 'task_type' in kwargs:
        task_type = kwargs['task_type']
    if 'color' in kwargs:
        color = kwargs['color']
    
    USES_DATES = False    
    if np.issubdtype(start.dtype, np.datetime64) and np.issubdtype(finish.dtype, np.datetime64):
        start = mdates.date2num(start)
        finish = mdates.date2num(finish)
        USES_DATES = True

    delta = finish - start

    fig,ax = plt.subplots(figsize=(9, 5))

    labels = task
    for i, task in enumerate(task):
        if color:
            c = color[task_type[i]] 
        else:
            c = None
        ax.broken_barh([(start[i], delta[i])], (i-0.4,0.8), color=c)

    # Set yticks
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels) 

    # Set xticks formatting
    # TODO: use matplotlib.dates.AutoDateFormatter
    if USES_DATES:
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        fig.autofmt_xdate()

    ax.invert_yaxis()
