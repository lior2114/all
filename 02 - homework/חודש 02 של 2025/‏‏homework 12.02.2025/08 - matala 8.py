#לשאול את המורה
sentence = input("Enter a sentence: ")
char_count = {}

for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

most_common_char = max(char_count, key=char_count.get)
print(f"The most common character is '{most_common_char}' which appears {char_count[most_common_char]} times.")