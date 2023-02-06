#!/usr/bin/python3

"""You have n number of locked boxes in front of you. Each box is
numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False"""

#if __name__=="__main__":

    #def canUnlockAll(boxes):
        #return boxes.count(3)
#boxes = [[1], [2], [3], [4], []]
#print(canUnlockAll(boxes))

"""
boxes = [[1], [2], [3], [4], []]
boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
for elements in boxes:
    print (elements)
print(boxes)
print(boxes[0])
print(type(boxes[0]))
print('')
print(boxes2[2][1])
print(boxes[3][0])
print(len(boxes[0]))
print(len(boxes2[0]))
"""
def canUnlockAll(boxes):
    array = []
    n = 0
    for b in boxes:
        for elements in b:
            array.append(elements)
    array.sort()
    for A in array:
        if array[n] <= array[n+1]:
            continue
        else:
            return False
    return True
