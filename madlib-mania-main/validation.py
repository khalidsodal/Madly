def validate_number():
    while True:
        user_input = input('Type a number:')
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Thats's not a valid number. Please try again.")

def get_validated_input(max_str_length, min_str_length, inputPrompt):
    user_input = inputPrompt.strip()
    if len(user_input) < min_str_length or len(user_input) > max_str_length:
        print(
            f'''
            Input length must be more than {min_str_length}
            and less than {max_str_length} characters
            '''
        )
        return False
    if not all(char.isalnum() for char in user_input):
        print('Input should not contain special characters')
        return False 
    return True    