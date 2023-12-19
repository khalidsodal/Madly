from simple_term_menu import TerminalMenu
from madlibs import *
from validation import *


def show_the_rules():
    """
    Shows the rules of the game
    """
    print(f'''
    1.Follow the instructions!
    2.Type the words carefully!
    ''')


show_the_rules()


def main():
    """ Main program function"""
    # Welcome message
    # Shows welcoming message
    print(f'''Welcome to Madlib Mania!''')
    user_name = ""
    # Ask for user's name
    valid_user_name = False
    while valid_user_name is False:
        user_name = input('Please enter your name:')
        if get_validated_input(100, 2, user_name):
            valid_user_name = True
        else:
            get_validated_input(100, 2, user_name)

    print(f'''Hello, {user_name.capitalize()},
    please pick an option from the menu''')
    options = ['1.Instructions', '2.Start Game', '3.Quit']
    main_menu = TerminalMenu(options)
    sub_options = ['1.Story 1', '2.Story 2', '3.Story 3', '4.Go Back']
    sub_menu = TerminalMenu(sub_options)
    quitting = False
    while quitting is not True:
        menu_index = main_menu.show()
        options_choice = options[menu_index]
        if options_choice == '3.Quit':
            print(f'Hope you enjoyed the game {user_name}!')
            quitting = True
        elif options_choice == '1.Instructions':
            show_the_rules()
        else:
            suboptions_index = sub_menu.show()
            sub_options_choice = sub_options[suboptions_index]
            ready_message = f'Get ready to type'
            end_message = f'You have reached the end of the story'
            if sub_options_choice == '1.Story 1':
                print(ready_message)
                madlib()
                print(end_message)
            elif sub_options_choice == '2.Story 2':
                print(ready_message)
                madlib_2()
                print(end_message)
            elif sub_options_choice == '3.Story 3':
                print(ready_message)
                madlib_3()
                print(end_message)
            else:
                menu_index = main_menu.show()


main()
