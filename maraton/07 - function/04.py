print("=======A========")
def som(massage,counter):
    for i in range(counter):
        print(f"the massage is: {massage}")

print("=======B========")
som("hi",3)

print("=======C========")
mass = input("enter the massage you want to show: ")
number = int(input("enter the number of times the massage will be printing: "))
som(mass,number)