import config
import child_info
from validation import Validation
import user_input
import prompts







def choose_story(child) -> str:
    """Prints a list of stories to the console and lets the user pick one

    Args:
        child (dict): contains child info

    Returns:
        str: file path to the chosen story
    """
    if child.sex == 'm':
        stories = list(config.male_stories.keys())
        story = user_input.pick_from_list(prompts.CHOOSE_STORY, stories)
        story_num = stories.index(story)
        return config.male_stories[stories[story_num]]

    else:
        stories = list(config.female_stories.keys())
        story = user_input.pick_from_list(prompts.CHOOSE_STORY, stories)
        story_num = stories.index(story)
        return config.female_stories[stories[story_num]]


def new_story() -> bool:
    """Let's the user choose if another story shoud be displayed by calling the
    select_input function

    Returns:
        bool: True if another story is required, False otherwise
    """
    new = user_input.select_input(prompts.NEW_STORY, prompts.YES_NO_OPTIONS)
    if new.upper() == 'YES':
        return True
    else:
        return False


def delete_child_option() -> bool:
    """Let's the user choose if child data should be deleted

    Returns:
        bool: True if data should be deleted, False otherwise
    """
    delete = user_input.select_input(prompts.DELETE, prompts.YES_NO_OPTIONS)
    if delete.upper() == 'YES':
        return True
    else:
        return False


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
