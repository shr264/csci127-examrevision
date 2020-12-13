#CSci 127 Teaching Staff
#October 2018
#Count which cars got the most parking tickets

#Import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = "tickets.csv"			#Name of the CSV file
tickets = pd.read_csv(csvFile)		#Read in the file to a dataframe
print(tickets) 				#Print out the dataframe
##Try running your program. It should print out all the information about all the tickets issued. Let's focus in on just licence plates. Change the last line of your program to be:

print(tickets["Plate ID"])	#Print out licence plates
##When you run the program again, you should just see the row number and licence plate recorded for each row.

##We want to refine this further to print how many tickets each car got. Pandas has a function just for counting occurrences, called value_counts(). Let's modify our last line again to use it:

print(tickets["Plate ID"].value_counts())	#Print out plates & number of tickets each got
##Rerunning the program, there are a lot of cars that got only a single ticket. If you scroll back up the Python shell, you will see the cars with the most tickets are listed first. Let's just print out the 10 cars that got the most tickets. We can do this by slicing to [:10]:

print(tickets["Plate ID"].value_counts()[:10])	#Print 10 worst & number of tickets