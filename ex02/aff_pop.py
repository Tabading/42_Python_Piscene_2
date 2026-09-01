
import matplotlib.pyplot as plt
from load_csv import load
import numpy as np
import pandas as pd


def remove_dates(data: pd.DataFrame):
    '''Remove Index dates in data above 2050.'''
    for i in data.index:
        if int(i) > 2050:
            data.drop(index=i, inplace=True)


def plot_countrys(country: str, other: str):
    '''Load the .csv, get the data for 2 given Indexes, and plot them.'''
    df = load("population_total.csv")

    c1 = df[df['country'] == country].iloc[0]
    c1 = c1.replace({'M': '', 'K': ''}, regex=True)
    c1_total = c1.iloc[1:].astype(float)
    remove_dates(c1_total)
    c1_years = c1_total.index.astype(int)

    c2 = df[df['country'] == other].iloc[0]
    c2 = c2.replace({'M': '', 'K': ''}, regex=True)
    c2_total = c2.iloc[1:].astype(float)
    remove_dates(c2_total)
    c2_years = c2_total.index.astype(int)

    plt.plot(c1_years, c1_total, color="g", label=country)
    plt.plot(c2_years, c2_total, label=other)


def format_plot():
    '''Format the Graph acording to subject specifications.'''
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    xticks = np.arange(1800, 2041, 40)
    yticks = np.arange(20, 81, 20)
    plt.xticks(xticks)
    plt.yticks(yticks, labels=[f'{x}M' for x in yticks])
    plt.legend(loc='lower right')


def main():
    try:
        plot_countrys("Germany", "France")
        format_plot()
        plt.show()

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
