'''
PART 1: ETL
- This code sets up the datasets for Problem Set 4
- NOTE: You will update this code for PART 4: CATEGORICAL PLOTS
'''

import pandas as pd

def extract_transform():
    """
    Extracts and transforms data from arrest records for analysis

    Returns:
        - `pred_universe`: The dataframe containing prediction-related data for individuals
        - `arrest_events`: The dataframe containing arrest event data
        - `charge_counts`: A dataframe with counts of charges aggregated by charge degree
        - `charge_counts_by_offense`: A dataframe with counts of charges aggregated by both charge degree and offense category
    """
    # Extracts arrest data CSVs into dataframes
    pred_universe = pd.read_csv('https://www.dropbox.com/scl/fi/a2tpqpvkdc8n6advvkpt7/universe_lab9.csv?rlkey=839vsc25njgfftzakr34w2070&dl=1')
    arrest_events = pd.read_csv('https://www.dropbox.com/scl/fi/n47jt4va049gh2o4bysjm/arrest_events_lab9.csv?rlkey=u66usya2xjgf8gk2acq7afk7m&dl=1')

    # Creates two additional dataframes using groupbys
    charge_counts = arrest_events.groupby(['charge_degree']).size().reset_index(name='count')
    charge_counts_by_offense = arrest_events.groupby(['charge_degree', 'offense_category']).size().reset_index(name='count')
    
    return pred_universe, arrest_events, charge_counts, charge_counts_by_offense

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

def felony_updates(pred_universe: pd, arrest_events: pd):
    '''
    Takes the arrest_events dataframe and processes the data to see if any arrest cluster contains a felony charge

    Parameters:
    - pred_universe dataframe
    - arrest_events dataframe

    Returns:
    - felony_charge dataframe: The dataframe containing the description of arrests events by if they contain felony charges
    - pred_universe_update dataframe: The merged dataframe from felony_charge and the provided pred_universe
    '''

    # Creating felony_charge dataframe from arrest_events dataframe
    felony_charge: pd = arrest_events.groupby('arrest_id')['charge_degree'].apply(lambda x: 1 if (x == 'felony').sum() > 0 else 0).reset_index(name = 'has_felony_charge')

    # Merging pre_universe dataframe with felony_charge dataframe
    pred_universe_update: pd = pred_universe.copy()
    pred_universe_udpate = pred_universe_update.merge(felony_charge, on = 'arrest_id', how = 'outer')

    # Returning updated dataframes
    return felony_charge, pred_universe_udpate
    

