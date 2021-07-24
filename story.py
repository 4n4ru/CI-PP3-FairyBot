import config
from child_info import ChildInfo
import textwrap as tr
import prompts
import user_input

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

def choose_story(stories) -> str:
    """Prints a list of stories to the console and lets the user pick one

    Args:
        stories (list): a list of stories 

    Returns:
        str: file path to the chosen story
    """
    story = user_input.pick_from_list(prompts.CHOOSE_STORY, stories)
    story_num = stories.index(story)
    return config.male_stories[stories[story_num]]


def generate_story(child, story) -> str:
    """Reads a string from the story path and replaces placeholder keys from
    with values from the child dictionary

    Args:
        child (dict): dictionary
        story (str): filepart to the chosen story
    Returns:
        str: A custom story filled with info from the child dictionary
    """
    child_dict = child.make_dictionary()
    with open(story) as f:
        story = f.read()
    custom_story = story.format(**child_dict)
    return custom_story


def choose_child(profiles) -> int:
    """Prints a list of names to the console and lets the user pick one

    Args:
        profiles (list): a list containing all the child info dictionaries

    Returns:
        int: the index of the dictionary for the chosen child within the list
    """
    options = []
    for child in profiles:
        options.append(child.name)
    options.append('Add new child')
    chosen = user_input.pick_from_list(prompts.CHOOSE_CHILD, options)
    ind = options.index(chosen)
    return ind

def story():
    while True:
        chosen = choose_child(config.profiles)
        while chosen == len(config.profiles):
            child = ChildInfo.add_child()
            config.profiles.insert(-1, child)
            chosen = choose_child(config.profiles)
        if config.profiles[chosen].sex == 'm':
            chosen_story = choose_story(config.male_stories.keys())
        else:
            chosen_story = choose_story(config.female_stories.keys())
        story = generate_story(config.profiles[chosen], chosen_story)
        print(tr.fill(story, 70))
        
        if new_story():
            continue
        else:
            while delete_child_option() and len(config.profiles) > 0:
                if len(config.profiles) == 1:
                    print(prompts.NO_DELETE)
                    break
                else:
                    print(ChildInfo.delete_child(config.profiles))
            break

story()