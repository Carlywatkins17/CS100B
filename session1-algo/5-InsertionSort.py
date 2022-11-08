# insertion sort
# sort items as you would cards -- find the right place for a card
#    compared to the other sorted cards, and shift cards to make room.
def insertionsort(list):
    for i in range(1, len(list)):
        number = list[i]
        pos = i
        while pos > 0 and list[pos-1] > number:
            list[pos] = list[pos-1]
            pos = pos - 1
        list[pos] = number