#hard coded זה אומר שהם בתוך הליסט כבר שאני בוחר בהם 

listing = {15:"corn", 10:"table", 15:"ball"}
code = int(input("enter a code for your product: "))
name = input("enter a product name: ")
listing.update({code:name})
print(listing)

code2 = int(input("enter a code for search your product: "))
if code2 in listing.keys():
    #ככה מציג את השם שמופיע ליד המספר (value)
    print(listing [code2])
    #ככה מציג רק את המספר שבחרנו
    print(code2)
else:
    print("the product you search are not in the list")