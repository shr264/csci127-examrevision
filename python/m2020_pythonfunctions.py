import matplotlib.pyplot as plt
import random

def cumulativeSum(start, max):
    sum = start
    sumlist = [start]

    #repeatedly double the sum until the cumulative sum is greater than n*max where n is a randomly generater integer
    n = random.randrange(100)
    while sum < n*max:
        sum = 2*sum
        sumlist.append(sum)

    return sumlist

def main():

    #ask user for an interger and store it in start
    start = int(input('Please enter an interger: '))

    #ask user for an interger and store it in max
    max = int(input('Please enter an interger: '))

    #call cuumulativeSum with start and max 
    #store the return in sumlist
    sumlist = cumulativeSum(start, max)

    plt.plot(sumlist)
    plt.show()

if __name__ == "__main__":
    main()