import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data")

    # Line of best fit using ALL data (1880-2050)
    slope1, intercept1, r_value1, p_value1, se1 = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    years_extended1 = range(df["Year"].min(), 2051)
    sea_level_pred1 = [slope1 * year + intercept1 for year in years_extended1]
    ax.plot(years_extended1, sea_level_pred1, color="red", label="Best Fit Line (1880-2050)")

    # Line of best fit using data from 2000 onwards
    df_2000 = df[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, se2 = linregress(
        df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"]
    )
    years_extended2 = range(2000, 2051)
    sea_level_pred2 = [slope2 * year + intercept2 for year in years_extended2]
    ax.plot(years_extended2, sea_level_pred2, color="green", label="Best Fit Line (2000-2050)")

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save and return
    plt.savefig("sea_level_plot.png")
    return ax
