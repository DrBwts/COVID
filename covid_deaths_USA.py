# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:30:14 2020

@author: Nic Bwts
"""

# "CDC.csv"
# https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-Week-Ending-D/r8kw-7aab
# Deleted the whole country stats & just left the stats for the states

# "Pop_Density.csv"
# https://raw.githubusercontent.com/camillol/cs424p3/master/data/Population-Density%20By%20State.csv 
# I added NYC pop density = 26403 to the GIT hub file from Wiki page

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Covid death data from CDC
CV_data              = pd.read_csv("CDC.csv", usecols=[4, 6, 7])
CV_data['CV_Deaths'] = CV_data['CV_Deaths'].fillna(0)
CV_states            = CV_data.groupby('State')
CV_data_agg          = CV_states.aggregate(np.sum)
CV_data_agg_no_outs  = CV_data_agg.drop(['New York City', 'District of Columbia'])
CV_per_Total         = CV_data_agg['CV_Deaths']/CV_data_agg['Total_Deaths'] * 100

# Population data GIT hub
pop_data = pd.read_csv("Pop_Density.csv", usecols=[2, 3])
pop_data.set_index('State', inplace=True)
pop_no_outs = pop_data.drop(['New York City', 'District of Columbia'])

# Pearson Correlation Coefficient
R         = pearsonr(CV_data_agg['CV_Deaths'], pop_data['Density'])
R_p       = pearsonr(CV_per_Total, pop_data['Density'])
R_no_outs = pearsonr(CV_data_agg_no_outs['CV_Deaths'], pop_no_outs['Density'])

#plt.scatter(pop_data['Density'], CV_data_agg['CV_Deaths'])
plt.scatter(pop_data['Density'], CV_per_Total)