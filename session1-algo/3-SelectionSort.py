import random

# selection sort
#   starting at the beginning, search for the smallest item,
#      then swap it for the first. Then do the same for each
#      spot in the array.
def selectionsort(list):
    for i in range(0, len(list)):
        min = i
        #look for an item smaller than list[min]
        for j in range(i, len(list)):
            if list[j] < list[min]:
                min = j     #just remember where this was
        #we've found it. Swap it into this location
        tmp = list[i]
        list[i]=list[min]
        list[min] = tmp

def main():
    numbers = []
    # let's make a list of random numbers
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    print(numbers[0:10])
    selectionsort(numbers)
    print(numbers[0:10])

if __name__ == '__main__':
    main()