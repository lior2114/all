sen = input("enter a sentence: ")
char_count = {}

for ch in sen:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
 
max_char = ''
max_count = 0 

for ch,value in char_count.items():
    if value >= max_count:
        max_count = value
        max_char = ch 
print(f"the most common char in the sentence is: {max_char}, and its showing {max_count} times")
print (char_count)

 