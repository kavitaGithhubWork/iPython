#find first duplicate number 

def findfirstduplicate(str):

    dup = {} #define a a dictionary
    
    for char in str:
        if char in dup:
            dup[char] += 1
        else:
            dup[char] = 1
    for char in dup: 
        if dup[char] == 1:
            return char

    
print (findfirstduplicate('madame'))