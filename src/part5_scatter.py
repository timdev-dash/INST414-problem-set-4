'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
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

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
def felony_nonfelony_scatterplot(pred_universe: pd):
    '''
    Produces a scatter plot comparing the predictions to commit felony and nonfelony crimes, 
    colored by if their rearrest was for a felony

    Parameters:
    - pred_universe dataframe

    Returns:
    - Scatterplot with hue by current felony charge status
    '''

    # Resetting seaborn settings before starting
    sns.reset_defaults()
    seaborn_settings()

    sns.lmplot(data=pred_universe, 
               x='prediction_felony', 
               y='prediction_nonfelony',
               hue = 'y_felony')
    plt.savefig('./data/part5_plots/current_felony_scatterplot.png', bbox_inches='tight')
        
    # Closing the plot to prevent overwriting
    plt.close()

    # In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
    print('The group on the right side of the plot are predicted to be more likely to both commit felony and non-felony crimes. ' +
          'A likely follow would be to see if the rearrest rates for felonies and nonfelonies compared with the predictions align.')

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
def felony_rearrest_scatterplot(pred_universe: pd):
    '''
    Produces a scatter plot comparing the predictions to commit felony and if their rearrest was for a felony

    Parameters:
    - pred_universe dataframe

    Returns:
    - Scatterplot of the felony arrest prediction compared to results
    '''
    
    # Resetting seaborn settings before starting
    sns.reset_defaults()
    seaborn_settings()

    sns.lmplot(data=pred_universe, 
            x='prediction_felony', 
            y='y_felony')
    plt.savefig('./data/part5_plots/felony_rearrest_scatterplot.png', bbox_inches='tight')
        
    # Closing the plot to prevent overwriting
    plt.close()

    # In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
    print('It appears that the resulting plot does not show any applicable detail to the broader issue. Because ' +
          'the question of the predictions accuracy cannot be easily summarized by creating a scatter plot of a ' +
          'data with a binary base case. Someone is either rearrested or not. You will end up with clumping at the '+
          'top and bottom of the scatterplot.')