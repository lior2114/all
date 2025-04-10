def longest_string_length(strings):
    max_length = 0
    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
    return max_length

list1 = ["apple", "banana", "cherry"]
list2 = ["dog", "elephant", "frog"]
list3 = ["house", "igloo", "jungle"]

result1 = longest_string_length(list1)
result2 = longest_string_length(list2)
result3 = longest_string_length(list3)

print(result1)
print(result2)
print(result3)