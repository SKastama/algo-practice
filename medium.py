# Question 1
def function1(string1, string2):
    output= ""
    char2= set(string2)
    for i in range(len(string1)):
        if string1[i] not in char2:
            output+= string1[i]
    return output

# print(function1("abcdegfhijk", "abfg"))


    
