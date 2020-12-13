"""
number 7
"""
import pandas as pd


def readDataFrame():
    """Prompts the user for the name of the input file.
Reads the dataframe.
Returns the dataframe."""
    inFile = input('Enter input file name: ')
    salaries = pd.read_csv(inFile)
    return(salaries)


def alterDataFrame(df):
    """ Prompts the user for the name of the new column.
Computes the new column as the overtime paid salary
(base salary * 1.5 * OT hours).
Returns the dataframe with the new column and the new column’s name. """
    newColName = input('Enter the name of the new column: ')
    df[newColName] = (df['Base Salary'] * 1.5) * df['OT Hours']
    return(df, newColName)

def printColumnAverage(df, column):
    """ Prints the average of the column."""
    avg = df[column].mean()
    print(avg)


def main():
    df = readDataFrame()
    df2, newColName = alterDataFrame(df)
    printColumnAverage(df2, newColName)


if __name__ == '__main__':
    main()