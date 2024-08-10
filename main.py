'''
- You will run Problem Set 4 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()
    
    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    # 1
    part3.fta_barplot(pred_universe)

    # 2
    part3.hued_barplot(pred_universe)

    # 3
    part3.age_histogram(pred_universe)

    # 4
    part3.spec_bin_histogram(pred_universe)

    ##  PART 4: CATEGORICAL PLOTS  ##
    felony_charge, pred_universe_felony = part1.felony_updates(pred_universe, arrest_events)

    # 1
    part4.charge_type_felre_catplot(pred_universe_felony)

    # 2
    part4.charge_type_nonfelre_catplot(pred_universe_felony)

    # 3
    part4.hued_charge_type_catplot(pred_universe_felony)

    ##  PART 5: SCATTERPLOTS  ##
    # 1
    
    # 2


if __name__ == "__main__":
    main()
