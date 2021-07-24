import config
import child_info
from validation import Validation
import user_input
import prompts




def delete_child(profiles) -> str:
    """Prints a list of names for the user to choose from and deletes the
    chosen item from the list

    Args:
        profiles (list): list of dictionaries with child info

    Returns:
        str: returns success message
    """
    names = []
    for child in profiles:
        names.append(child.name)
    chosen = user_input.pick_from_list(prompts.DELETE_CHILD, names[:-1])
    ind = names.index(chosen)

    del config.profiles[ind]
    confirm = f'The child {chosen} was successfully deleted'
    return confirm
