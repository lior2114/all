from class1 import Lighter

lighter1 = Lighter("red","20", "50%",2)
lighter2 = Lighter("yellow","40", "60%",4)

lighter1.power_up()
lighter1.power_down()
lighter1.switch_battery()
lighter1.details()
print(lighter1)
lighter1.write_file()

lighter2.power_up()
lighter2.power_down()
lighter2.switch_battery()
lighter2.details()
print(lighter2)
lighter2.write_file()