import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns

def create_count_amount_pareto(df_raw, 
                               group_col, 
                               xlabel=None,
                               return_agg_df = False
                              ):
    """Function to create pareto analysis on specific group of transaction
    :df_raw: Raw dataframe before aggregated
    :group_col: Columm which is used as the x-axis of the analysis
    :count_col: Column that contains count of trx
    :amount_col: Column that contains amount of trx
    """
    
    ### CREATE DATA AGGREGATION ###
    df = df_raw.groupby(
        [group_col],
        as_index = False,
        observed = True
    ).agg(
        count=('trx_amount', 'size'),
        tot_daily_amount = ('trx_amount', 'sum')
        )

    df = df.sort_values('tot_daily_amount', ascending=False)
    df['cum_pct_trx_amount'] = round(df['tot_daily_amount'].cumsum() / df['tot_daily_amount'].sum() * 100, 2)
#     df['cum_pct_trx_count'] = round(df['count'].cumsum() / df['count'].sum() * 100, 2)
    
    #### START CREATING CHART ####
    fig = plt.figure(figsize=(20,5))

    ### FIRST CHART
    ax = fig.add_subplot(121)
    # Plot bars (i.e. frequencies)
    ax.bar(df[group_col], df['tot_daily_amount'])
    ax.set_title(f"{xlabel} by Total Transaction Amount") 
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Total Trx Amount");

    # Second y axis (i.e. cumulative percentage)
    ax2 = ax.twinx()
    ax2.plot(df[group_col], df['cum_pct_trx_amount'], color="red", marker="D", ms=7)
    ax2.axhline(80, color="orange", linestyle="dashed")
    ax2.yaxis.set_major_formatter(PercentFormatter());

    ### SECOND CHART
    
    df = df.sort_values('count', ascending=False)
#     df['cum_pct_trx_amount'] = round(df['tot_daily_amount'].cumsum() / df['tot_daily_amount'].sum() * 100, 2)
    df['cum_pct_trx_count'] = round(df['count'].cumsum() / df['count'].sum() * 100, 2)
    
    ax_1 = fig.add_subplot(122)
    # Plot bars (i.e. frequencies)
    ax_1.bar(df[group_col], df['count'])
    ax_1.set_title(f"{xlabel} by Total Transaction Count") # 
    ax_1.set_xlabel(xlabel) # "Age Group"
    ax_1.set_ylabel("Total Trx Count");

    # Second y axis (i.e. cumulative percentage)
    ax_12 = ax_1.twinx()
    ax_12.plot(df[group_col], df['cum_pct_trx_count'], color="red", marker="D", ms=7)
    ax_12.axhline(80, color="orange", linestyle="dashed")
    ax_12.yaxis.set_major_formatter(PercentFormatter())
    ax_12.set_ylabel("Cumulative Percentage");
    
    ## Rotate xlabel
    ax.tick_params(axis='x', labelrotation = 45)
    ax_1.tick_params(axis='x', labelrotation = 45)
    
    if return_agg_df:
        return df