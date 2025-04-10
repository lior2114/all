import os
def data(name,lastname,email,phone):
    if not isinstance(name,str) or not isinstance(lastname,str):
        raise ValueError("enter only strings")
    if not isinstance (phone,str) or isinstance (email, int):
        raise ValueError("enter only number in phone number/ email cant be only only numers")
    folder_name = "user_data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    with open (f"./{folder_name}/user_data.txt", "w") as data_file:
        data_file.write(f"your name: {name}, your lsat name: {lastname},\n yout email: {email}, your phone number: {phone}")
    
    lis = []
    with open(f"./{folder_name}/user_data.txt", "r") as data_file:
        for line in data_file:
            lis.append(line.strip())
    return lis
 