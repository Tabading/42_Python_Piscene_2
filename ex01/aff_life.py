
import matplotlib.pyplot as plt
from load_csv import load


def main():
    try:
        df = load("life_expectancy_years.csv")
        country = "Germany"

        ger = df[df['country'] == country].iloc[0]
        years = ger.index[1:].astype(int)
        life_expectancy = ger.iloc[1:].astype(float)

        # print(ger)
        # print("years:", years.values)
        # print("life_expectancy:", life_expectancy.values)

        plt.plot(years, life_expectancy, label=country)
        plt.title("Life Expectancy in Germany")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy (years)")
        plt.legend()
        plt.show()

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
