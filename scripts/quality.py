import os
import shutil
import statistics
from collections import Counter

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredText
from matplotlib.ticker import MaxNLocator

inputFolder = './data'
outputFolder = './output'
data = pd.read_excel(f'{inputFolder}/data.xlsx')

prettyPrintDatapoint = {
    'Q1' : 'Q1 (DT)',
    'Q2' : 'Q2 (Sim)',
    'Q3' : 'Q3 (AI)',
    'Q4' : 'Q4 (Challenges)'
}


def chartQualityData(data, settings):
    categories = ['Quality']
    (variables, color, fileName) = settings[0]
    
    plotData = {}
    counter = []
    
    for variable in variables:
        counter.append((variable, round(data[variable].mean(), 3)))
        #counter.append((variable, round(data[variable].std(), 3)))
    
    counter.reverse()
    plotData['Quality'] = counter
    
    numCharts = len(plotData.keys())
    rows = [len(p) for p in plotData.values()] #The height ratios of the rows are set proportionally to the rows their display.
    
    #Create subplots
    fig, axs = plt.subplots(nrows=numCharts, sharex=False, gridspec_kw={'height_ratios': rows})
    
    #If only 1 subplot, still manage it as an array for compatibility reasons.
    if len(categories) == 1:
        axs = [axs]

    """
    Plotting
    """
    for i, category in enumerate(plotData):
        counter = plotData[category]
        
        values = [element[1] for element in counter]
        sumFrequencies = sum(values)
        print(counter)
        tab = '\t'
        labels = [f'{(prettyPrintDatapoint[element[0]] if element[0] in prettyPrintDatapoint.keys() else element[0])} \u2014 {element[1]} ({round((element[1]/sumFrequencies)*100)}%)' for element in counter]
        #Get the regular labels and values by: labels, values = zip(*counter)
        
        print(labels)
        
        #Prepare bar chart
        indexes = np.arange(len(labels))
        width = 0.75
        axs[i].set_xlim([0, sum(values)*0.8])   #scales bars to 100% within one subplot
        
        #Create vertical bar chart
        plt.sca(axs[i])
        plt.barh(indexes, values, width, color=color)
        plt.yticks(indexes, labels, rotation=0)

        """
        Title of the chart shown as a rotated Y axis label on the right side, inside of the plot area
        """
        title = category.capitalize()
        #right label placement:
        #axs[i].yaxis.set_label_position("right")
        #plt.ylabel(title, rotation=270, fontsize=12, labelpad=-30)
        #left label placement:
        axs[i].yaxis.set_label_position("left")
        plt.ylabel(title, rotation=90, fontsize=12, labelpad=7)
        
        """
        Left here in case we'd need to revert to anchored text from right-side inner Y label
        """
        #anchored_text = AnchoredText(title, loc= titleLabelPosition[category] if category in titleLabelPosition.keys() else "center right")
        #anchored_text = AnchoredText(title, loc="center right")
        #axs[i].add_artist(anchored_text)
        
        #Remove plot area borders
        axs[i].spines['right'].set_visible(False)
        axs[i].spines['top'].set_visible(False)
        axs[i].spines['bottom'].set_visible(False)
        #Remove X ticks and labels
        plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
        
        """
        Category label settings
        """
        #Y tick labels inside
        axs[i].tick_params(axis="y", direction="out", pad=-10)
        #no Y ticks
        axs[i].yaxis.set_ticks_position('none') 
        #align Y tick labels to the left
        ticks = axs[i].get_yticklabels()
        axs[i].set_yticklabels(ticks, ha = 'left')

        """
        Tick label font management
        """
        ax = plt.gca()
        labels=ax.get_yticklabels()+ax.get_xticklabels()
        for label in labels:
            label.set_fontsize(13)
        
        """
        Sizing and plotting
        """
        figure = plt.gcf()
        #Height proportional to the number of rows displayed
        figure.set_size_inches(8, 0.33*sum(rows))
        plt.gcf().tight_layout()

    plt.savefig('{}/{}.pdf'.format(outputFolder, fileName))
    #plt.show()  #Turn this off in final code or make it optional
    

chartQualityData(data, [
    (['Q1', 'Q2', 'Q3', 'Q4'], '#ffdd47', 'quality'),
    #(['Domain'], '#85d4ff', 'domain'),
    ]
)