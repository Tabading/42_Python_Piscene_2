*This project has been created as part of the 42 advanced curriculum by tabading.*

# Table of Contents
- [Description](#description)
    - [Project Specifications](#project-specifications)
    - [Mandetory Modules](#mandetory-modules)
        - [Ex00](#ex00)
        - [Ex01](#ex01)
        - [Ex02](#ex02)
        - [Ex03](#ex03)
- [Instructions](#instructions)
    - [Venv](#venv)
    - [Compilation](#compilation)
    - [Norm](#norm)
- [Resources](#resources)
    - [KI Usage](#ki-usage)


# Description
*Training Piscine Python for Data Science - 2* is the third of 5 Projects, serving as an intoduction to Data Tables. It encompasses 4 mandetory Modules.

### Project Specifications
For each Project these additional Rules must be followed:
- No code in the global scope. Use functions!
- Each program must have its main and not be a simple script: 

        def main():
            # your tests and your error handling

        if __name__ == "__main__":
            main()

- Any exception not caught will invalidate the exercises, even in the event of an error
that you were asked to test.
- All your functions must have documentation (\_\_doc\_\_)
- Your code must follow the norm
    - pip install flake8
    - python3 -m flake8 file.py
- For this module, we will use data from FREE SCHOOL MATERIALS FROM GAPMINDER.ORG, CC-BY LICENSE.

## Mandetory Modules

### Ex00
Learn to load and print a Dataset from a .csv file.

#### Pandas
Pandas is a Python library used for working with data sets. \
It has functions for analyzing, cleaning, exploring, and manipulating data.

### Ex01
Manipulate a Pandas data set for specific values and display them as a grap with matplotlib.

#### Code explanation:
ger = dataframe[dataframe['country'] == "Germany"].iloc[0]: \
- dataframe[dataframe['country'] == "Germany"]: find the row with index Germany
- iloc[0]: converts that row into a Series.
- contains indexed values

years = ger.index[1:].astype(int)
- take all indexes starting at position 1 as ints
- contains the indexes AS values

life_expectancy = ger.iloc[1:].astype(float)
- take ger starting at postion 1 as floats
- contains indexed values 

plt.plot(years, life_expectancy, label="Germany")
- basic form is: plt.plot(x, y, format_string, **kwargs)
- x: x axis 
- y: y axis
    - they get paired togeter to form points (x, y) and connected by a line
- label: gives the line a name 
    - displayed with plt.legend()
- format_string: these can be combined together like so "ro--"
    - color: changes line color, 
        - "r" red
        - "g" green
        - "b" blue
        - "c" cyan
        - "m" magenta
        - "y" yellow
        - "k" black
        - "w" white
    - linestyle: changes the line
        - "-"  solid
        - "--" dashed
        - ":"  dotted
        - "-." dash-dot
    - linewidth / lw: 
    - marker: markes coordinate on line
        - "o" circle
        - "." point
        - "s" square
        - "^" triangle up
        - "v" triangle down
        - "*" star
        - "+" plus
        - "x" x
        - "D" diamond
- markersize / ms
- markerfacecolor: inside of marker
- markeredgecolor / mec : outline of marker
- markeredgewidth / mew: width of marker outline
- alpha: transparency


### Ex02
Format the Matplotlib plot/Graph to specifications.

### Ex03
Learn to manipulate the scale and ticks of a graph, with matplotlib.

# Instructions

### Venv
Create a Venv with all required libs, unless you want to install them  globaly.

- python3 -m venv venv
- source venv/bin/activate
- pip install pandas
- pip install matplotlib
- pip install flake8
- deactivate (to exit)


### Compilation

    python3 *.py

### Norm 

    python3 -m flake8 *.py

# Resources
ex00:
- https://www.w3schools.com/python/pandas/pandas_dataframes.asp

ex01:
- https://matplotlib.org/stable/tutorials/pyplot.html
- https://github.com/pandas-dev/pandas/blob/v3.0.5/pandas/plotting/_core.py#L772-L2154
- https://www.w3schools.com/python/pandas/pandas_plotting.asp
- KI to help understand plt.plot

ex02:
- https://matplotlib.org/stable/users/explain/axes/axes_ticks.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html

ex03:
- https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html
- https://matplotlib.org/stable/gallery/scales/scales.html
- https://matplotlib.org/stable/gallery/ticks/tick-locators.html

### KI Usage
KI was generally used to save time searching for specific functions, explaining specifics, figuring out what what i'm trying to do is called and finding shorter solutions, ie. how MY code could be reformated to be shorter/less lines for learning purposes.