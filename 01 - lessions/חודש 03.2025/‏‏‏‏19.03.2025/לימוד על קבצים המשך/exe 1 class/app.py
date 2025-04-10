import ramkol as ra       
try:           
        speaker1 = ra.Speaker("tony", "jbl", "red",100)
        speaker2 = ra.Speaker("steve", "sony", "blue", 80)
        print(speaker1.display())
        print(speaker2.display())
        # speaker1.volume_up()
        # speaker2.volume_up()
        speaker1.create_file()
        speaker2.create_file()
        ra.Speaker.show_counter() #כמה אובייקטים יש לנו כל פעם כשקוראים לclass של הספיקר 


except ValueError as err:
        print(err)
except Exception as err:
    print(err)
