# Question 1
def function1(string1, string2):
    output= ""
    char2= set(string2)
    for i in range(len(string1)):
        if string1[i] not in char2:
            output+= string1[i]
    return output

# print(function1("abcdegfhijk", "abfg"))

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
    
