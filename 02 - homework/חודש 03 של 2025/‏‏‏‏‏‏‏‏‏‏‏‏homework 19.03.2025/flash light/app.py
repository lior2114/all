import flash_light as fla

try:
    flash_light1 = fla.Flashlight("log1","Red", 10, 100, 2)
    flash_light2 = fla.Flashlight("log2","Blue", 12, 150, 3)
    flash_light1.display()
    flash_light2.display()
    # print(flash_light1.__str__())
    # print(flash_light2.__str__())
    flash_light1.light_up()
    flash_light2.light_up()
    flash_light1.light_off()
    flash_light2.light_off()
    fla.Flashlight.show_counter()
    flash_light1.switch_battery()
    flash_light2.switch_battery()
    flash_light2.switch_battery()
    flash_light2.switch_battery()
    flash_light2.switch_battery()
    flash_light1.create_file() # שמתי בסוף כדי שיתעדכנו הסוללות שהורדנו בשורות הקודמות 
    flash_light2.create_file() # שמתי בסוף כדי שיתעדכנו הסוללות שהורדנו בשורות הקודמות 
except ValueError as err:
    print(err)
except Exception as err:
    print(err)