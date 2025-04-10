colored_items = [
    {"shirt":"red","pants":"red", "scarf":"red"},
    {"shoes":"yellow","vr":"yellow", "screen":"yellow"},
    {"apple":"green", "lemon":"green"}
]
for words in colored_items:
    for key,value in words.items():
        print(f"{key}:{value}" , end = " | ")
    print()
        
counter = None
for words in colored_items:
    for i in words:
        if counter is None or len(i) < len(counter):
            counter = i 
print(counter)

#לשאול את המורה 
max_length = 0
longest_items = []
for words in colored_items:
    for i in words:
        if len(i) > max_length:
            max_length = len(i)
            longest_items = [i] 
        elif len(i) == max_length:
            longest_items.append(i)

for item in longest_items:
    print(item)

