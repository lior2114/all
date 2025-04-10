print("==========A=========")
def some_sentence(lis):
    maxx = 0
    the_list = '' #עם גרשים כדי שיכניס את המילים לשם 
    for chars in lis:
        if len(chars) > maxx:
            maxx = len(chars) 
            the_list = chars
    return the_list

print("==========B=========")
for i in range(3):
    listed = []
    for j in range(3):
        n = input(f"enter word {j+1} for list number {i+1}: ")
        listed.append(n)
    x = some_sentence(listed)
    print(f"the longes word in the list is: {x}")

