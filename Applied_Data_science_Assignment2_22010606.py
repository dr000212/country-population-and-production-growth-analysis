# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 02:23:34 2023

@author: Deepak Raj Palaniammal Kaliannan
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


worldbankdata = pd.read_excel(r'C:\Users\user\Downloads\assignment2data.xlsx')


def describe_dataframe(dataframe):
    """
   Prints descriptive statistics and covariance matrix for a given dataframe.

   Args:
       dataframe (pandas.DataFrame): The dataframe to describe.

   Returns:
       None"""

    # Calculate descriptive statistics
    summary = dataframe.describe()

    # Calculate kurtosis and skewness
    kurtosis = dataframe.kurtosis()
    skewness = dataframe.skew()

    # Calculate covariance matrix
    covariance = dataframe.cov()

    # Add kurtosis and skewness to summary
    summary.loc['kurtosis'] = kurtosis
    summary.loc['skewness'] = skewness

    # Print summary and covariance matrix
    print('Descriptive Statistics:')
    print(summary)
    print('\nCovariance Matrix:')
    print(covariance)


describe_dataframe(worldbankdata)


def clean_transpose(df):
    """
    Transpose a dataframe, remove any rows or columns that contain only NaN values,
    and replace any remaining NaN values with zero.

    Parameters:
    -----------
    df : pandas.DataFrame
        The input dataframe to be cleaned and transposed.

    Returns:
    --------
    pandas.DataFrame
        The cleaned and transposed dataframe.
    """
    # Transpose the dataframe
    transposed = df.transpose()

    # Remove any rows or columns that contain only NaN values
    cleaned = transposed.dropna(how='all').T.dropna(how='all')

    # Replace any remaining NaN values with zero
    cleaned = cleaned.fillna(0)

    return cleaned


transposeddata = clean_transpose(worldbankdata)
#print( transposeddata)

year = []
value = []
indicator_code = []
indicator_name = []
country_code = []
country_name = []
years = ['1980', '1981', '1982', '1983', '1984', '1985', '1986',
         '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
         '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
         '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
         '2014']
new_dataframe = pd.DataFrame()
for idx in years:
    dataframe2 = transposeddata[[
        'Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', idx]]
    dataframe2.columns = ['Country Name', 'Country Code',
                          'Indicator Name', 'Indicator Code', 'value']
    dataframe2['year'] = [idx for i in range(len(dataframe2))]

    new_dataframe = pd.concat([new_dataframe, dataframe2], axis=0)


def barplot1(year, country_name, indicator_name, df):
    """
    Generate a bar plot showing the CO2 emission from solid fuel consumption as a percentage of total CO2 emissions
    for the given countries, years, and indicator name.

    Parameters:
    -----------
    year : list of str
        The years to include in the plot.
    country_name : list of str
        The country names to include in the plot.
    indicator_name : str
        The name of the indicator to plot.
    df : pandas.DataFrame
        The input dataframe containing the data to plot.

    Returns:
    --------
    None
    The function only plots the CO2 emission from solid fuel consumption as a percentage of total CO2 emissions
    for the given countries,and does not return any value."""

    c_dataframe = df[df['Indicator Name'] == indicator_name]
    c_dataframe3 = pd.DataFrame()
    for idx in country_name:
        c_dataframe2 = c_dataframe[c_dataframe['Country Name'] == idx]
        c_dataframe3 = pd.concat([c_dataframe3, c_dataframe2], axis=0)

    c_dataframe4 = pd.DataFrame()
    for idx in year:
        c_dataframe2 = c_dataframe3[c_dataframe3['year'] == idx]
        c_dataframe4 = pd.concat([c_dataframe4, c_dataframe2], axis=0)

    plt.figure(figsize=(25, 15))
    colors = ['#6e40aa', '#1b9e77', '#d95f02',
              '#7570b3', '#e7298a', '#66a61e', '#e6ab02']
    plt.title("Co2 Emission From Solid Fuel Consumption Percent")
    sns.barplot(data=c_dataframe4, x="Country Code",
                y="value", hue="year", palette=colors)
    plt.ylabel("Co2 Emission Percent")
    plt.legend()
    plt.savefig('Barplot1.png')
    plt.show()
    return None


year = ["1970", "1980", "1990", "2000", "2010", "2020"]
country_name = ["India", "China", "Japan", "Australia", "Belgium", "France",
                "United Kingdom", "New Zealand", "Canada", "Turkiye", "United States", "South Africa"]
indicator_name = 'CO2 emissions from solid fuel consumption (% of total)'
barplot1(year, country_name, indicator_name, new_dataframe)


def barplot2(year, country_name, indicator_name, df):
    """
   Creates a bar plot of CO2 emission from gaseous fuel consumption for a given list of countries and years.

   Parameters:
   year (list): A list of strings representing the years to be included in the plot.
   country_name (list): A list of strings representing the names of countries to be included in the plot.
   indicator_name (str): A string representing the name of the indicator for which the plot is to be created.
   df (pd.DataFrame): A pandas dataframe containing the data for the plot.

   Returns:
   None
   The function only plots CO2 emission from gaseous fuel consumption for a given list of countries and years and does not return any value."""
    c_dataframe = df[df['Indicator Name'] == indicator_name]
    c_dataframe3 = pd.DataFrame()
    for idx in country_name:
        c_dataframe2 = c_dataframe[c_dataframe['Country Name'] == idx]
        c_dataframe3 = pd.concat([c_dataframe3, c_dataframe2], axis=0)

    c_dataframe4 = pd.DataFrame()
    for idx in year:
        c_dataframe2 = c_dataframe3[c_dataframe3['year'] == idx]
        c_dataframe4 = pd.concat([c_dataframe4, c_dataframe2], axis=0)

    plt.figure(figsize=(25, 10))
    colors1 = ['blue', 'red', 'yellow', 'orange', 'pink', 'green', 'brown']
    plt.title("Co2 Emission From Gaseous Fuel Consumption Percent")
    sns.barplot(data=c_dataframe4, x="Country Code",
                y="value", hue="year", palette=colors1)
    plt.ylabel("Co2 Emission Percent")
    plt.legend()
    plt.savefig('Barplot2.png')
    plt.show()
    return None


year = ["1970", "1980", "1990", "2000", "2010", "2020"]
country_name = ["India", "China", "Japan", "Australia", "Belgium", "France",
                "United Kingdom", "New Zealand", "Canada", "Turkiye", "United States", "South Africa"]
indicator_name = 'CO2 emissions from gaseous fuel consumption (% of total)'
barplot2(year, country_name, indicator_name, new_dataframe)


# country wise population growth trend
c_dataframe = new_dataframe[new_dataframe['Indicator Name']
                            == "Urban population (% of total population)"]
c_dataframe.index = [i for i in range(len(c_dataframe))]


def lineplot1(country_name):
    """
    Plots a line graph showing the urban population percent in total population for the specified countries over time.

    Args:
    - country_name: A list of strings containing the names of the countries to be plotted.

    Returns:
    - None
    The function only shows the urban population percent in total population for the specified countries, 
    and does not return any value."""

    c_dataframe3 = pd.DataFrame()
    for idx in country_name:
        c_dataframe2 = c_dataframe[c_dataframe['Country Name'] == idx]
        c_dataframe3 = pd.concat([c_dataframe3, c_dataframe2], axis=0)

    plt.figure(figsize=(25, 10))
    plt.xticks(rotation='vertical')
    plt.title("Urban Population Percent in Total Population")
    sns.lineplot(data=c_dataframe3, x="year", y="value", hue="Country Code")
    plt.xlabel("YEARS")
    plt.ylabel("POPULATION GROWTH")
    plt.legend()
    plt.savefig('Lineplot1.png')
    plt.show()
    return None


country_name = ['Aruba', "Afghanistan",
                "Arab World", "india", "china", "Australia"]
country_name1 = ["United Arab Emirates", "Argentina", "Brazil", "Cuba",
                 "Germany", "Spain", "United Kingdom", "Mexico", "Russian Federation"]
lineplot1(country_name=country_name1)


# country wise population growth trend
c_dataframe = new_dataframe[new_dataframe['Indicator Name']
                            == "Electricity production from coal sources (% of total)"]
c_dataframe.index = [i for i in range(len(c_dataframe))]


def lineplot2(country_name):
    """
    Plots a line graph of the electricity production from coal sources over the years for the specified countries.

    Parameters:
    -----------
    country_name : list
        A list of strings containing the names of countries to be plotted.

    Returns:
    --------
    The function only shows the, electricity production from coal sources over the years for the specified countries.  
    and does not return any value."""

    c_dataframe3 = pd.DataFrame()
    for idx in country_name:
        c_dataframe2 = c_dataframe[c_dataframe['Country Name'] == idx]
        c_dataframe3 = pd.concat([c_dataframe3, c_dataframe2], axis=0)

    plt.figure(figsize=(25, 15))
    plt.title(" ELECTRICITY PRODUCTION FROM COAL SOURCES ")
    # color3 = [   "#0000FF",    "#FFFF00",    "#008000",    "#FFA500",    "#FF0000",    "#A52A2A",    "#E6D5B8",    "#800080",    "#FFC0CB",    "#808080",    "#ADD8E6"]
    plt.xticks(rotation='vertical')
    sns.lineplot(data=c_dataframe3, x="year", y="value", hue="Country Code")
    plt.xlabel("YEARS")
    plt.ylabel("PERCENTAGE")
    plt.legend()
    plt.savefig('Lineplot2.png')
    plt.show()
    return None


country_name = ['Aruba', "Afghanistan",
                "Arab World", "india", "china", "Australia"]
country_name1 = ["United Arab Emirates", "Argentina", "Brazil", "Cuba", "Germany",
                 "Egypt, Arab Rep.", "Spain", "United Kingdom", "Korea, Rep.", "Mexico", "Russian Federation"]
lineplot2(country_name=country_name1)
