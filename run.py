import config
import child_info
from validation import Validation
import user_input
import prompts

def add_child() -> dict:
    """Creates a child dictionary by calling different functions for user input

    Returns:
        dict: info about the child
    """

    name = user_input.input_string(prompts.ENTER_NAME).capitalize()
    friend = user_input.input_string(prompts.ENTER_FRIEND).capitalize()
    color = user_input.pick_from_list(prompts.ENTER_COLOR, prompts.COLORS)
    food = user_input.input_string(prompts.ENTER_FOOD)
    animal = user_input.input_string(prompts.ENTER_ANIMAL)
    sport = user_input.input_string(prompts.ENTER_SPORT)
    disliked_food = user_input.input_string(prompts.ENTER_DISLIKED_FOOD)
    sex = user_input.select_input(prompts.ENTER_SEX, prompts.SEX_OPTIONS)
    
    child = child_info.ChildInfo(
        name, friend, color, food, animal, sport, disliked_food, sex)
    return child.make_dictionary()


def choose_child(profiles) -> int:
    """Prints a list of names to the console and lets the user pick one

    Args:
        profiles (list): a list containing all the child info dictionaries

    Returns:
        int: the index of the dictionary for the chosen child within the list
    """
    names = []
    for child in profiles:
        names.append(child['name'])
    chosen = user_input.pick_from_list(prompts.CHOOSE_CHILD, names)
    ind = names.index(chosen)
    return ind


def generate_story(child, story) -> str:
    """Reads a string from the story path and replaces placeholder keys from
    with values from the child dictionary

    Args:
        child (dict): dictionary
        story (str): filepart to the chosen story
    Returns:
        str: A custom story filled with info from the child dictionary
    """
    with open(story) as f:
        story = f.read()
    custom_story = story.format(**child)
    return custom_story


def choose_story(child) -> str:
    """Prints a list of stories to the console and lets the user pick one

    Args:
        child (dict): contains child info

    Returns:
        str: file path to the chosen story
    """
    if child['sex'] == 'm':
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
        names.append(child['name'])
    chosen = user_input.pick_from_list(prompts.DELETE_CHILD, names[:-1])
    ind = names.index(chosen)

    del config.profiles[ind]
    confirm = f'The child {chosen} was successfully deleted'
    return confirm
