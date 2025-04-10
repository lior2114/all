import os
try:
    # #אופציה א
    '''
    בלי משתנים 
    '''
    # with open("./data/details.txt", 'w') as file:
    #     file.write(input("enter your first name: ")+ "\n")
    #     file.write(input("enter your last name: ")+ "\n")
    #     file.write(input("enter your email: ")+ "\n")
    #     file.write(input("enter your phone: ")+ "\n")



    #אופציה ב
    '''
    עם משתנים 
    '''
    first_name = (input("enter your first name: ")+ "\n")
    last_name = (input("enter your last name: ")+ "\n")
    mail = (input("enter your mail: ")+ "\n")
    phone_nubmer = (input("enter your phone number: ")+ "\n")

    # name_of_folder = "data"
    # if not os.path.exists(name_of_folder):
    #     os.makedirs(name_of_folder)

    listed = []
    with open("./details.txt", 'w') as file:
        file.write(first_name)
        file.write(last_name)
        file.write(mail)
        file.write(phone_nubmer)
# צריך להציג אותו במצב קריאה כדי שיוכל להוסיף אותו לליסט 
    with open("./details.txt", 'r') as file:
        for line in file:
            listed.append(line)
    print(listed)



except Exception as err:
    print(err)
