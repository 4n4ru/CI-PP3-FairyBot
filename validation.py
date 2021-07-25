class Validation:
    """Contains methods for validating user input
    """

    def validate_num_input(self, user_input, max_num) -> bool:
        """Checks if the user input is a number between 1 and max_numd

        Args:
            user_input (str): input provided by the user
            max_num (int): maximum allowed number for the user input

        Raises:
            ValueError: Raises an error if the number is out of range.

        Returns:
            bool: False if an error was rised, True otherwise
        """

        try:
            num = int(user_input)
            if num < 1 or num > max_num:
                raise ValueError(
                    f'This should be a number between 1 and {max_num}!')
        except ValueError as e:
            print(f'Invalid data: {e}, please try again.\n')
            return False
        return True

    def validate_str_input(self, user_input) -> bool:
        """Checks if the user input is a valid string with a minimum length of 2
        characters

        Args:
            user_input (str): input provided by the user

        Returns:
            bool: False if the input is invalid, True otherwise
        """
        if (not user_input.isalpha()) or len(user_input) < 2:
            print(
                'Your input should be a single word of a minimum of 2'
                'characters.'
                'Please try again.')
            return False
        return True

    def validate_str_select(self, user_input, answer_set) -> bool:
        """Checks if the user input is in a given answer set

        Args:
            user_input (str): input provided by the user
            answer_set (tuple): a set containing all the allowed answers

        Returns:
            bool: False if the user input is not in the given set, true
            otherwise
        """
        if user_input not in answer_set:
            print('Invalid input. Please try again.')
            return False
        return True
