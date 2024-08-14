'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
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
    sns.set_palette(sns.color_palette("viridis"))

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def charge_type_felre_catplot(pred_universe_felony: pd):
    '''
    Produces catplot of charge type and felony rearrest prediction from provided dataframe

    Parameters:
    - pred_universe_felony dataframe

    Returns:
    - charge_type catplot
    '''

    # Resetting seaborn settings before starting
    sns.reset_defaults()
    seaborn_settings()

    sns.catplot(data=pred_universe_felony,
                x='has_felony_charge',
                y='prediction_felony', 
                kind='bar')
    plt.savefig('./data/part4_plots/charge_type_felre_catplot.png', bbox_inches='tight')
    
    # Closing the plot to prevent overwriting
    plt.close()

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
def charge_type_nonfelre_catplot(pred_universe_felony: pd):
    '''
    Produces catplot of charge type and felony rearrest prediction from provided dataframe

    Parameters:
    - pred_universe_felony dataframe

    Returns:
    - charge_type catplot
    '''

    # Resetting seaborn settings before starting
    sns.reset_defaults()
    seaborn_settings()

    sns.catplot(data=pred_universe_felony,
                x='has_felony_charge',
                y='prediction_nonfelony', 
                kind='bar')
    plt.savefig('./data/part4_plots/charge_type_nonfelre_catplot.png', bbox_inches='tight')
    
    # Closing the plot to prevent overwriting
    plt.close()

    # In a print statement, answer the following question: What might explain the difference between the plots?
    print('It is strange that those with a felony arrest were less likely to have been predicted to have a felony arresst when' + 
          ' comparing to those with a misdemeanor arrest. It could be that longer jail terms for felony arestees is expected' + 
          ' to decrease the likelihood of recidivism during due to their incarceration')


# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
def hued_charge_type_catplot(pred_universe_felony: pd):
    '''
    Produces catplot of charge type and felony rearrest prediction from provided dataframe

    Parameters:
    - pred_universe_felony dataframe

    Returns:
    - charge_type catplot
    '''

    # Resetting seaborn settings before starting
    sns.reset_defaults()
    seaborn_settings()

    sns.catplot(data=pred_universe_felony,
                x='has_felony_charge',
                y='prediction_felony',
                hue='y_felony', 
                kind='bar')
    plt.savefig('./data/part4_plots/hued_charge_type_catplot.png', bbox_inches='tight')
    
    # Closing the plot to prevent overwriting
    plt.close()

    # In a print statement, answer the following question: 
    # What does it mean that prediction for arrestees with a current felony charge, 
    # but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
    # but who did get rearrested for a felony crime?
    print('It would appear that a having a past felony charge is a higher indicator of future felony charges than ' +
          'having a past misdemeanor charge.')