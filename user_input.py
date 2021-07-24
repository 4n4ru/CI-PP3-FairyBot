from validation import Validation
import prompts

def pick_from_list(prompt, list) -> str:
    """[summary]

    Args:
        prompt (str): [description]
        list (list): [description]

    Returns:
        str: [description]
    """
    while True:
        print(f'{prompt}')
        for ind in range(len(list)):
            print(f'{ind+1}. {list[ind]}')
        chosen = input(prompts.ENTER_NUMBER)
        if Validation.validate_num_input(chosen, len(list)):
            break
    chosen_ind = int(chosen) - 1
    return list[chosen_ind]