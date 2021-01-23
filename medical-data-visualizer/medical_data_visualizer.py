import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight']/(df['height']/100)**2 > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol']==1,'cholesterol']=0
df.loc[df['cholesterol']>1, 'cholesterol']=1

df.loc[df['gluc']==1,'gluc']=0
df.loc[df['gluc']>1, 'gluc']=1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).agg('size').rename(columns={'size':'total'})



    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x = 'variable',
    y = 'total',
    kind='bar',
    hue='value',
    col = 'cardio',
    data = df_cat)

    fig = g.fig

    #####or without group and reformat by 'cardio'
    # g = sns.catplot(x='variable', 
    # col="cardio",
    # data=df_cat,
    # kind="count", 
    # hue ='value')
    # g.set_axis_labels('variable','total')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_hi']>=df['ap_lo']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))





    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))


    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', square=True, linewidths=.5, cbar_kws={"shrink": .5})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
