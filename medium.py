# Question 1
def function1(string1, string2):
    output= ""
    char2= set(string2)
    for i in range(len(string1)):
        if string1[i] not in char2:
            output+= string1[i]
    return output

# print(function1("abcdegfhijk", "abfg"))


# Question 1: Alternative way but cant repeat charactors
def function1Alternate(string1, string2):
    char1= set(string1)
    char2= set(string2)
    result= char1 - char2
    return "".join(sorted(list(result)))

# print(function1Alternate("abcdegfhijk", "abfg"))


# Question 2
def function2(string):
    charCount= {}
    for i in range(len(string)):
        if string[i] not in charCount:
            charCount[string[i]]= 0
        charCount[string[i]]+= 1
    for key, val in charCount.items():
        if val == 1:
            return key

# print(function2("aabb"))


# Question 3
def function3(string):
    longest= 0
    current= ""
    start= 0
    while start < len(string):
        for i in range(start, len(string)):
            if string[i] in current:
                longest= max(longest, len(current))
                current= ""
                break
            else:
                current+= string[i]
        start+= 1
    return longest

# print(function3("Hello there"))

# Question 3: Alternative and optimized way
def function3Alternative(string):
    longest= 0
    current= ""
    start= 0
    idx= start
    while start < len(string):
        if idx >= len(string):
            start+= 1
            idx= start
        elif string[idx] in current:
            longest= max(longest, len(current))
            current= ""
            start+= 1
            idx= start
        else:
            current+= string[idx]
            idx+= 1
    return longest

# print(function3Alternative("Hello there"))

# Algo expert
# Number 13
def minHeightBst(array):
    return callMinHeightBst(array, 0, len(array)-1)
	
def callMinHeightBst(array, start, end):
	if start > end:
		return
	middle= (end+start)//2
	tree= BST(array[middle])
	tree.left= callMinHeightBst(array, start, middle-1)
	tree.right= callMinHeightBst(array, middle+1, end)
	return tree
	
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# Number 25
def kadanesAlgorithm(array):
    maxEndHere= array[0]
    maxSoFar= array[0]
    for i in range(1, len(array)):
        maxEndHere+= array[i]
        maxEndHere= max(maxEndHere, array[i])
        maxSoFar= max(maxSoFar, maxEndHere)
    return maxSoFar

# print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))


# Number 26
def hasSingleCycle(array):
    idxsSeen= set()
    i= 0
    while True:
        newIdx= (i + array[i])%(len(array))
        if newIdx not in idxsSeen:
            idxsSeen.add(newIdx)
        else:
            return False
        if len(idxsSeen) == len(array):
            break
        i= newIdx
    return True
    
# print(hasSingleCycle([1, 2]))

# Number 27 in progress
# def riverSizes(matrix):
#     riverLen= []
#     riverIdxs= [[False for value in row] for row in matrix]
#     localLen= 0
#     nodeRow= 0
#     nodeCol= 0
#     i= nodeRow
#     j= nodeCol
#     while nodeRow < len(matrix):
#         if riverIdxs[i][j] == False and matrix[i][j] == 1:
#             riverIdxs[i][j]= True
#             localLen+= 1
#             if i+1 < len(matrix) and matrix[i+1][j] == 1 and riverIdxs[i+1][j] == False:
#                 i+= 1
#             elif i-1 >= 0 and matrix[i-1][j] == 1 and riverIdxs[i-1][j] == False:
#                 i-= 1
#             elif j+1 < len(matrix[i]) and matrix[i][j+1] == 1 and riverIdxs[i][j+1] == False:
#                 j+= 1
#             elif j-1 >= 0 and matrix[i][j-1] == 1 and riverIdxs[i][j-1] == False:
#                 j-= 1
#             else:
#                 riverLen.append(localLen)
#                 localLen= 0
#                 if j+1 < len(matrix[i]):
#                     nodeCol+=1
#                     j= nodeCol
#                 elif j+1 == len(matrix[i]) and i+1 < len(matrix):
#                     nodeRow+= 1
#                     i= nodeRow
#                     nodeCol= 0
#                     j= nodeCol
#                 elif i+1 == len(matrix):
#                     break
#         elif riverIdxs[i][j] == False and matrix[i][j] == 0:
#             riverIdxs[i][j]= True
#         else:
#             if j+1 < len(matrix[i]):
#                 nodeCol+=1
#                 j+= 1
#             elif j+1 == len(matrix[i]) and i+1 < len(matrix):
#                 nodeRow+= 1
#                 i+= 1
#                 nodeCol= 0
#                 j= 0
#             elif i+1 == len(matrix):
#                 break
#     print(riverIdxs)
#     return riverLen

# matrix1= [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0]
# ]
# print(riverSizes(matrix1))