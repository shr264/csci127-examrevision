"""
 Fill in the following functions that are part of a program that analyzes NYC Urban Forest of
street trees (from NYC OpenData):
• getData(): asks the user for the name of the CSV file and returns a DataFrame of the
contents.
• biggestDiameter(): returns the largest diameter (tree dbh) in the DataFrame, and
• makeGraph(): makes a plot of the x versus y columns specified.
"""

import pandas as pd
def getData():
    """
    Asks the user for the name of the CSV and
    Returns a dataframe of the contents.
    """
    fileName = input('Enter file name: ')
    df = pd.read_csv(fileName)
    return(df)


def biggestDiameter(df):
    """
    Takes a DataFrame as input and
    Returns the maximum value in
    the column, tree_dbh.
    """
    M = df['tree_dbh'].max()
    return(M)


def makeGraph(df,xCol,yCol):
    """
    Makes a pyplot plot of x versus y column in DataFrame df
    """
    df.plot(x = xCol, y = yCol)