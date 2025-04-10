print("=======C=======")
def remove_number(listed, number):
    new_list = []
    if len(listed) == 0:
      raise TypeError ("enter numbers!")
    for i in listed:
        if not isinstance(i, int):# אם הוא לא מספר 
            raise TypeError("enter only numbers!")
    for i in listed:
      if number != i:
        new_list.append(i)
    return new_list


# # print("=======C2=======")
# def remove_number2(listed2, number2):
#     if len(listed2) == 0:
#       raise TypeError ("enter numbers!")
#     for i in listed2:
#         if not isinstance(i, int):# אם הוא לא מספר 
#             raise TypeError("enter only numbers!")
#     while number2 in listed2:
#        listed2.remove(number2)
