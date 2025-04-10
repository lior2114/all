from rps_game import Game as g
try:
    game_instance = g()  # Create an instance of the Game class
    user_choice = game_instance.get_user_choice()
    comp_choice = game_instance.get_computer_choice()
    print(f"{game_instance.user_name} chose: {user_choice}")
    print(f"{game_instance.pc_name} chose: {comp_choice}")
    print(game_instance.determine_winner())

except ValueError as e:
    print(e)
except Exception as err:
    print(err)


                
        

                
        