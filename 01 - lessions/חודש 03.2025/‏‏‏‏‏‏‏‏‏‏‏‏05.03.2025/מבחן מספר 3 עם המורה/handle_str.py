#version 1 
def count_chr (word,ch):
    counter = 0
    for chars in word:
        if ch == chars:
            counter += 1
    return counter 


#version 2
def count_chrv2 (word,ch):
    #counter = word.count(ch) אפשרי גם 
    #return counter 
    return word.count(ch) #סופר כמה פעמים הצאר במילה 

print(count_chrv2("loilr", 'l'))