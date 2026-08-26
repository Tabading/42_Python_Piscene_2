
from load_csv import load


def main():
    try:
        print(load("life_expectancy_years.csv"))
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
