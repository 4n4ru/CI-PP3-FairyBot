import config
from child_info import ChildInfo
import textwrap as tr
import prompts
import user_input
import save_story

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

def choose_story(story_dict) -> str:
    """Prints a list of stories to the console and lets the user pick one

    Args:
        story_dict (dict): A dictionary with all the stories that are available

    Returns:
        str: file path to the chosen story
    """
    story = user_input.pick_from_list(
        prompts.CHOOSE_STORY, list(story_dict.keys()))
    return story_dict[story]


def generate_story(child, story) -> str:
    """Reads a string from the story path and replaces placeholder keys with
    values from the child dictionary

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
    """Prints a list of options to the console and lets the user pick one

    Args:
        profiles (list): a list containing all the child info objects

    Returns:
        int: the index of the object for the chosen child within the list
    """
    options = []
    for child in profiles:
        options.append(child.name)
    options.append('Add new child')
    chosen = user_input.pick_from_list(prompts.CHOOSE_CHILD, options)
    ind = options.index(chosen)
    return ind

def story():
    """Main function for creating a custom story.
    Lets the user choose a child, if the user chooses to add a new child the
    function add_child is called. After a child is chosen, lets the user pick a
    story depending on the child sex. Generates the story using the chosen
    child object and story. Prints the story to the terminal. Gives the user an
    option to save the story for later. If this is chosen the user is given a
    user id. Asks the user if another story should be provided. Ask the user if
    a child object should be deleted and calls a function to delete the child
    object.
    """
    while True:
        chosen = choose_child(config.profiles)
        while chosen == len(config.profiles):
            child = ChildInfo.add_child()
            config.profiles.append(child)
            chosen = choose_child(config.profiles)
        if config.profiles[chosen].sex == 'm':
            chosen_story = choose_story(config.male_stories)
        else:
            chosen_story = choose_story(config.female_stories)
        story = generate_story(config.profiles[chosen], chosen_story)
        print(tr.fill(story, 70))
        
        save = save_story.save_story_option()
        if save:
            user_id = save_story.save_story(story)
            print(prompts.SUCCESS_SAVE + user_id)

        if new_story():
            continue
        else:
            while delete_child_option() and len(config.profiles) >= 0:
                if len(config.profiles) == 0:
                    print(prompts.NO_DELETE)
                    break
                else:
                    print(ChildInfo.delete_child(config.profiles))
            break

story()