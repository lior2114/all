def max_product_price(dict):
    if len(dict) == 0:
        raise ValueError ("dictionary is empty! (in fucnction at the start)")
    maxx = 0
    max_word = ' '
    for key,value in dict.items(): #אפילו שזה לא פועל האייטמס אם מכניסים דיקשינרי שזה מילון אז זה יעבוד 
        if value > maxx:
            maxx = value
            max_word = key
    tup = (max_word,maxx)
    return tup 

def max_product_priceV2(dict):
    if len(dict) == 0:
        raise ValueError ("dictionary is empty! (in fucnction at the start)")
    max_price = 0
    k = ''
    for key in dict:
        if dict[key]>= max_price:
            max_price = dict[key]
            k = key
    return k,max_price

a1 = {'apple1':500,'banana1': 600, 'peach1':100}
a2 = {'apple2':700,'banana2': 600, 'peach2':100}
a3 = {'apple3':500,'banana3': 600, 'peach3':800}

for1 = print(max_product_priceV2(a1))
print(for1)
for2 = print(max_product_priceV2(a2))
print(for2)
for3 = print(max_product_priceV2(a3))
print(for3)