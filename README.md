# (mawilliams7) Please put this code into a python file so it is easier to view.
# LabTwo#Rene Esquivel
#80219337
#CS 2302

#read the .txt files
fileA = open("vivendi.txt", 'r')
fileB = open("activision.txt", 'r')


#create the empty list
combinedList =[]

#add all the numbers in fileA
# (mawilliams7) Print statements below are unnecessary
for line in fileA:
    combinedList.append(line)
    print(len(combinedList))

#add all the numbers in fileB
for line in fileB:
    combinedList.append(line)
    print(len(combinedList))



#Given class for lab 2
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
        # (mawilliams7) I'm unsure what this conditional is doing. Please add comment to verify
        if i == (len(pythonList)-1):
            return currentNode
            prevNode = currentNode

def lengthLl(head):
    count = 0

    while head != None:
        count = count +1
        head = head.next
    print("Linked List had" + str(count) + "elements")

linkedlistHead = makePythonListIntoLL(combinedList)
lengthLl(linkedlistHead)

# (mawilliams7) I'm unsure why this method is necessary as it doesn't return anything
def compare_Each_Element(list):
    print("Compare each element")
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if list[i] == list[j]:
                print("Compared to others", list[i], " ", list[j])

linkedListHead = lengthLl(list)
compare_Each_Element(linkedListHead)


def bubble_Sort(numbers, numberSize):
    print("BubbleSort")
    for i in range(0, len(numberSize-1)):
        for j in range(0, len(numberSize-i-1)):
            if (numbers[j] > numbers[j+1]):
             temp = numbers[j]
             numbers[j] = numbers[j+1]
             numbers[j+1] = temp

linkedListHead = lengthLl(numbers, numberSize)
bubble_Sort(linkedListHead)


def merge_List(listOne, listTwo):

    print("MergeSort")
    temp = None

    if listOne is None:
        return listTwo
    if listTwo  is None:
        return listOne
    if listOne.data <= listTwo.data:
        temp = listOne
        temp.next = merge_List(listOne.next, listTwo)
    else:
        temp = listTwo
        temp.next = merge_List(listOne, listTwo.next)
    return temp

linkedListHead = lengthLl(listOne, listTwo)
merge_list(linkedListHead)


def merge_Sort(head):
    if head is None or head.next is None:
        return head

    listOne, listTwo = divide_List(head)
    listOne = merge_Sort(listOne)
    listTwo = merge_Sort(listTwo)
    head = merge_List(listOne, listTwo)
    return head

# (mawilliams7) I'm unsure what thus method is doing. I don't believe the return statement returns both values.
def divide_List(head):
    slow = head
    fast = head
    if fast:
        fast = fast.next

    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
            mid = slow.next
    slow.next = None
    return head, mid


def search(item, seen):

    seen = []
    # (mawilliams7) Since you are using item as a method paramater and as the iterator for this for loop,
    # there may be a collision between the two leading to a bad search.
    for item in range(len(seen)):
        seen[item] = True

    else:
        seen[item] = False

        print(seen[item])

linkedListHead = lengthLl(item, seen)
search(linkedListHead)




