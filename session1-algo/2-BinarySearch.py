import random
import string

# sequential search
#  look for an item and return where that item is in the list.
#  if it's not there, return -1
def sequentialsearch(haystack, needle):
    for i in range(0, len(haystack)):
        if (haystack[i] == needle):
            return i

    # if we went through the whole haystack, it must not be there
    return -1

def main():
    numbers = []
    # let's make a list of random numbers
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))


    target = random.randrange(0,2000)
    location = sequentialsearch(numbers, target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + " at location " + str(location))


if __name__ == '__main__':
    main()

# binary search
#  another searching algorithm. But if the data are sorted, we can
#    approach it differently. We can look at the middle item in the list
#    If it's smaller than our needle, we only need to search the upper half
#    If it's larger than our needle, we search the lower half.
#    Of course, if we have a match, we're done.
def binarysearch(haystack, needle):
    start = 0
    end = len(haystack)

    while start <= end:
        i = start + (end-start)//2
        if haystack[i] < needle:
            start = i+1
        elif haystack[i] > needle:
            end = i-1
        elif haystack[i] == needle:    
            
            #if we're out of the loop, we didn't find it
            return i

def main():
    numbers = []
    # let's make a list of random numbers
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    # sort the numbers so we can use binary search
    numbers.sort()
    target = random.randrange(0,2000)
    location = binarysearch(numbers, target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + " at location " + str(location))