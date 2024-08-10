'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def seaborn_settings():
    '''
    Applies the default seaborn theme and sets the default figure size
    '''
    sns.set_theme()
    sns.set(rc={'figure.figsize':(6, 4)})

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def fta_barplot(pred_universe: pd):
    '''
    Produces various types of bar plots using the given datasets

    Parameters:
    - pred_univers dataframe

    Returns:
    - fta Vertical barplot
    '''

    # Resetting seaborn settings before starting
    sns.reset_defaults()
    seaborn_settings()

    # Processes pred_universe to create data to chart fta column
    fta_counts: pd = pred_universe.groupby(['fta']).size().reset_index(name='count')

    sns.barplot(data=fta_counts, 
                x='fta',
                y='count')
    plt.savefig('./data/part3_plots/fta_vertical_barplot.png', bbox_inches='tight')

    # Closing the plot to prevent overwriting
    plt.close()

# 2. Hue the previous barplot by sex
def hued_barplot(pred_universe: pd):
    '''
    Produces various types of bar plots using the given datasets

    Parameters:
    - pred_universe dataframe

    Returns:
    - fta Vertical barplot with hue based on gender
    '''

    # Resetting seaborn settings before starting
    sns.reset_defaults()
    seaborn_settings()

    # Processes pred_universe to create data to chart fta column and gender
    fta_counts_by_gender = pred_universe.groupby(['fta', 'sex']).size().reset_index(name='count')

    sns.barplot(data=fta_counts_by_gender, 
                x='fta',
                y='count',
                hue='sex')
    plt.savefig('./data/part3_plots/hued_fta_vertical_barplot.png', bbox_inches='tight')

    # Closing the plot to prevent overwriting
    plt.close()

# 3. Plot a histogram of age_at_arrest
def age_histogram(pred_universe: pd):
    '''
    Produces different types of histograms using the given dataset

    Parameters:
    - pred_universe dataframe

    Returns:
    - Histogram of age_at_arrests without specifying bins
    '''

    # Resetting seaborn settings before starting
    sns.reset_defaults()
    seaborn_settings()

    sns.histplot(data=pred_universe, 
                 x='age_at_arrest')
    plt.savefig('./data/part3_plots/age_histogram.png', bbox_inches='tight')

    # Closing the plot to prevent overwriting
    plt.close()

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def spec_bin_histogram(pred_universe: pd):
    '''
    Produces different types of histograms using the given dataset

    Parameters:
    - pred_universe dataframe

    Returns:
    - Histogram of age_at_arrests with a specified number of bins
    '''

    # Resetting seaborn settings before starting
    sns.reset_defaults()
    seaborn_settings()

    sns.histplot(data=pred_universe, 
                 x='age_at_arrest', 
                 bins=[18, 21, 30, 40, 100])
    plt.savefig('./data/part3_plots/age_histogram_specific_bins.png', bbox_inches='tight')

    # Closing the plot to prevent overwriting
    plt.close()
