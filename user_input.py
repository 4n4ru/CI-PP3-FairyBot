from validation import Validation
import prompts

def pick_from_list(prompt, list) -> str:
    """Asks the user to pick from a list.
    Prints the prompt to the terminal and the elements of the list in a ordered
    list. Asks the user to select a number, validates that the input is correct
    and returns the chosen element from the list.

    Args:
        prompt (str): prompt for the user to choose from the list
        list (list): a list of options

    Returns:
        str: chosen element of the list
    """
    while True:
        print(f'{prompt}')
        for ind in range(len(list)):
            print(f'{ind+1}. {list[ind]}')
        chosen = input(prompts.SELECT_NUMBER)
        if Validation.validate_num_input(chosen, len(list)):
            break
    chosen_ind = int(chosen) - 1
    return list[chosen_ind]


def input_string(prompt) -> str:
    """Prompts for user input with a predefined string and a substring that is 
    passed as an argument. The prompt is repeated until the user provides a
    string that passes through validation.

    Args:
        substring (str): a sub string that is added to the question for the 
        user

    Returns:
        str: returns the user input as a string
    """
    while True:
        string = input(prompt)
        if Validation.validate_str_input(string):
            break
    return string


def select_input(prompt, options) -> str:
    """Prompts the user for imput using prompt_text passed as an argument. The 
    prompt is repeated until the input validates against the options passed as
    an argument

    Args:
        prompt(str): Prompt text for the user
        options (tuple): contains strings for validating user input

    Returns:
        str: a string containing the option chosen
    """
    while True:
        selected = input(prompt)
        if Validation.validate_str_select(selected, options):
            break
    return selected