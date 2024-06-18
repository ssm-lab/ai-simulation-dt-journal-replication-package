import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import os
from string import Template

inputFolder = './data'
outputFolder = './output'

class Analysis():
    def __init__(self):
        if not os.path.exists(outputFolder):
            os.mkdir(outputFolder)
    
    
    def loadData(self):
        df = pd.read_excel(f'{inputFolder}/data.xlsx')
        return df

    def papersPerYear(self):
        df = self.loadData()
        
        #years = df[['Publication year', 'Publication type']].value_counts().sort_index().to_frame().reset_index()
        #years.columns = ['year', 'type', 'papers']
        
        #years = years.pivot_table(values='papers', index = 'year', columns='type', aggfunc='first').fillna(0)
        
        years = df[['Publication year']].value_counts().sort_index().to_frame().reset_index()
        years.columns = ['year', 'papers']
        print(years)
        
        #ax = years.plot(kind='bar', stacked = True, rot=0)
        ax = years.plot(kind='bar', x="year", rot=0, color='#34cbed')
        
        ax.set_ylabel('Papers', fontsize=15)
        ax.set_xlabel('Years', fontsize=15)
        ax.bar_label(ax.containers[0], fontsize=12)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_legend().remove()
        
        figure = plt.gcf()
        figure.set_size_inches(10, 5)
        
        plt.savefig(f'{outputFolder}/papers-per-year.pdf', format='pdf', bbox_inches='tight')
        plt.show()
        
    
    def venuesAndPublishers(self):
        df = self.loadData()
        
        df = df[['Publication venue', 'Publication type', 'Publisher']]
        
        papersPerPublisher = df.groupby('Publisher').count().sort_values(by=df.columns[0], ascending=False).reset_index()[['Publisher','Publication type']]
        papersPerPublisher.columns = ['publisher', 'papers']
        
        
        papersPerVenue = df.groupby(['Publication venue', 'Publisher']).count().sort_values(by=df.columns[1], ascending=False).reset_index()[['Publication venue', 'Publisher','Publication type']]
        papersPerVenue.columns = ['venue', 'publisher', 'papers']
        
        #papersPerVenue = papersPerVenue[papersPerVenue['papers']>1]
        
        vals = papersPerVenue.astype(str).values
        rows = ''
        
        for val in vals:
            val[0] = val[0].replace('&', '\&')
            rows += f"{val[0]} & {val[1]} & {val[2]} \\\\\n"
            
        templateValues = {'rows' : rows}
        
        result = ""
        
        with open('templates/table-template.tex', 'r') as f:
            src = Template(f.read())
            result = src.substitute(templateValues)
        
        f = open(f'{outputFolder}/venues-table.tex', 'w')
        f.write(result)
        f.close()

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-o','--observation', help='Observation ID.', type=str, nargs=1)
    #parser.add_argument('-s','--stash', help='Stash results folder.', action='store_true')
    #args = parser.parse_args()
    
    #if args.stash:
    #   if os.path.exists(resultsPath) and os.path.isdir(resultsPath):
    #        shutil.rmtree(resultsPath)
    #    os.mkdir(resultsPath)
    
    analysis = Analysis()
    analysis.papersPerYear()
    #analysis.venuesAndPublishers()