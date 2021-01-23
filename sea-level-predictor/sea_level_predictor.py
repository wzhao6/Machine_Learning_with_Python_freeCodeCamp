import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision='legacy')


    # Create scatter plot
    plt.figure(figsize=(10, 10))
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)


    # Create first line of best fit
    res1 = linregress(x, y)
    x_extend = x.append(pd.Series(range(2014,2050)), ignore_index=True)
    plt.plot(x_extend, res1.intercept + res1.slope*x_extend, 'r', label='fitted line1')


    # Create second line of best fit
    x_recent = x[x>=2000]
    y_recent = y[x[x>=2000].index]
    res2 = linregress(x_recent, y_recent)
    x_extend = x_recent.append(pd.Series(range(2014,2050)), ignore_index=True)
    plt.plot(x_extend, res2.intercept + res2.slope*x_extend, 'k', label='fitted line2')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()