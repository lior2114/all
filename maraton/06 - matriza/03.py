print("========A=========")
colored_items = [
    {"bikes": "red", "television": "red", "rmdddddkol": "red"},
    {"car": "yellow", "banana": "yellow", "sun": "yellow", "duck": "yellow"},
    {"goal":"green", "wall":"green"}
]
for i in colored_items:
    print(i)

print("========B=========")
shortest_item = ''
shortest_length = float("inf") #מסמל מספר חיובי אין סופי ככה שכל מה שנשווה אליו יהיה קטן יותר ממנו
for words in colored_items:
    for key in words.keys():
        if len(key) < shortest_length:
            shortest_length = len(key)
            shortest_item = key
print(shortest_item)

print("========C=========")
new = []
longest = 0
for words in colored_items:
    for key in words.keys():
        if len(key) > longest:
            longest = len(key)
            new = [key]
        elif len(key) == longest:
            new.append(key)
print(new)

# longest_items = []
# longest = 0
# for words in colored_items:
#     for key in words.keys():
#         if len(key) > longest:
#             longest = len(key)
#             longest_items = [key]
#         elif len(key) == longest:
#             longest_items.append(key)
# print(longest_items)



# for words in colored_items:
#     for key, value in words.items():
#         for ch in key:
#             if ch in w:
#                 w[ch] -= 1
#             else:
#                 w[ch] = 0  
# print(w)