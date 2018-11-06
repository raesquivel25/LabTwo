# Rene Esquivel
# 80219337
# CS 2302


# Given class for lab 2
class Node(object):
    item = -1
    next = None

    def __init__(self, item, next):
        self.item = item
        self.next = next


def makePythonListIntoLL(pythonList):
    prevNode = Node(pythonList[0], None)
    currentNode = Node

    for i in range(1, len(pythonList)):
        currentNode = Node(pythonList[i], prevNode)

        if i == (len(pythonList) - 1):
            return currentNode

        prevNode = currentNode


def lengthLL(head):
    count = 0

    while head != None:
        count = count + 1
        head = head.next

    print("Linked List has " + str(count) + " elements\n")


def copyLL(origHead):
    prev = Node(origHead.item, None)
    current = None  # pointer for traversing
    origHead = origHead.next

    while origHead.next != None:
        current = Node(origHead.item, prev)
        prev = current
        origHead = origHead.next

    current = Node(origHead.item, prev)
    return current


def printLL(head):
    while head != None:
        print(str(head.item))
        head = head.next


def compare_Each_Element(list):
    out = open("output.txt", 'a')
    out.write("\nCompare each element\n")
    pointerA = list
    while pointerA != None:
        pointerB = pointerA.next
        while pointerB != None:
            if pointerA.item == pointerB.item:
                out.write("Compared to others " + str(pointerA.item) + " " + str(pointerB.item) + "\n")
            pointerB = pointerB.next
        pointerA = pointerA.next
    out.close()


def bubble_Sort(list):
    out = open("output.txt", 'a')
    out.write("\nBubble Sort\n")
    out.close()
    while True:
        pointer = list
        sorted = True
        while pointer.next != None:
            if (pointer.item > pointer.next.item):
                sorted = False
                temp = pointer.item
                pointer.item = pointer.next.item
                pointer.next.item = temp
            pointer = pointer.next

        if sorted: break
    return list


def checkForDuplicates(list):
    out = open("output.txt", 'a')
    pointer = list
    while pointer.next != None:
        if pointer.item == pointer.next.item:
            out.write("Compared to others " + str(pointer.item) + " " + str(pointer.next.item) + "\n")
        pointer = pointer.next
    out.close()


def count(node):
    count = 0

    while node != None:
        node = node.next
        count += 1

    return count


def mergeSort(list):
    if list == None or list.next == None:
        return list

    left, right = split(list)

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def split(list):
    mid = count(list) // 2
    midPointer = list
    # point to the first node from the second half and break tie from first half.
    while mid > 1:
        midPointer = midPointer.next
        mid = mid - 1
    # points right before middle
    prevPointer = midPointer
    # midPointer points to actual middle
    midPointer = midPointer.next
    # break the tie between lists
    prevPointer.next = None
    # return left and right
    return list, midPointer


def merge(left, right):
    # Just need something to tie to
    placeHolder = Node(0, None)
    current = placeHolder

    while left != None and right != None:
        if left.item > right.item:
            current.next = right
            right = right.next

        else:
            current.next = left
            left = left.next

        current = current.next

    if left == None:
        current.next = right

    elif right == None:
        current.next = left

    return placeHolder.next


def booleanCheck(list):
    out = open("output.txt", 'a')
    out.write("\nBoolean Check\n")
    seen = []
    # we know that one company has 0-5000 and the other has 0-6000. We can therefore know there
    # will be no collisions in the 5001 - 6000 area so we dont care
    for i in range(0, 5000):
        seen.append(False)

    while list != None:
        if list.item < 5000:
            if seen[list.item]:
                out.write("Collision: " + str(list.item) + "\n")
            seen[list.item] = True
        list = list.next
    out.close()


####################
####    Main    ####
####################

# read the .txt files
fileA = open("vivendi.txt", 'r')
fileB = open("activision.txt", 'r')

# overwrite previous output file
out = open("output.txt", 'w')

# create the empty list
combinedList = []

# add all the numbers in fileA
for line in fileA:
    combinedList.append(int(line))

out.write("Length after adding Vivendi: ")
out.write(str(len(combinedList)) + "\n")

# add all the numbers in fileB
for line in fileB:
    combinedList.append(int(line))

out.write("Length after adding Activision: ")
out.write(str(len(combinedList)) + "\n")

out.close()

originalLLHead = makePythonListIntoLL(combinedList)
lengthLL(originalLLHead)

CEELL = copyLL(originalLLHead)
compare_Each_Element(CEELL)

BSLL = copyLL(originalLLHead)
checkForDuplicates(bubble_Sort(BSLL))

out = open("output.txt", 'a')
out.write("\nMerge Sort")
out.close()

MSLL = copyLL(originalLLHead)
checkForDuplicates(mergeSort(MSLL))

BCLL = copyLL(originalLLHead)
booleanCheck(BCLL)