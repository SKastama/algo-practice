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
                print(current)
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
            print(current)
            current= ""
            start+= 1
            idx= start
        else:
            current+= string[idx]
            idx+= 1
    return longest

print(function3Alternative("Hello there"))