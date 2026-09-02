import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def projection_life():
    '''Display a displays the projection of life expectancy in relation \
to the gross domestic product of the year 1900 for each country.'''
    life = load("life_expectancy_years.csv")
    life = life["1900"]
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    income = income["1900"]

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    ax = plt.gca()
    ax.set_xscale("log")
    ax.set_xlim(300, 11000)
    ax.xaxis.set_major_locator(ticker.FixedLocator([300, 1000, 10000]))
    ax.set_xticklabels(["300", "1k", "10k"])
    plt.plot(income, life, ".", ms=12)


def main():
    try:
        projection_life()
        plt.show()
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
