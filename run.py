import config
import child_info
import validation

def pick_color() -> str:
    """Lets the user pick a color from a list printed to the console

    Returns:
        str: returns the chosen color as a string
    """
    while True:
        print('Please choose your childs favorite colour:')
        print('1. Blue')
        print('2. Pink')
        print('3. Yellow')
        print('4. Orange')
        color = input('Enter a number: \n')
        if validation.validate_num_input(color, 4):
            break
    color = int(color)
    if color == 1:
        return 'blue'
    elif color == 2:
        return 'pink'
    elif color == 3:
        return 'yellow'
    elif color == 4:
        return 'orange'


def add_child() -> dict:
    """Promts for user input in order to create a child profile

    Returns:
        dict: info about the child
    """
    while True:
        name = input('Please enter your childs name:\n').capitalize()
        if validation.validate_str_input(name):
            break

    while True:
        friend = input(
            'Please enter your childs best friends name:\n').capitalize()
        if validation.validate_str_input(friend):
            break

    color = pick_color()

    while True:
        food = input('Please enter your childs favourite food:\n')
        if validation.validate_str_input(food):
            break

    while True:
        animal = input('Please enter your childs favourite animal: \n')
        if validation.validate_str_input(animal):
            break

    while True:
        sport = input('Please enter your childs favourite team sport: \n')
        if validation.validate_str_input(sport):
            break

    while True:
        disliked_food = input('Please enter a food your child dislikes: \n')
        if validation.validate_str_input(disliked_food):
            break
    while True:
        sex = input('Is your child male or female? Please enter f\\m: \n')
        if validation.validate_str_select(sex, ('F', 'f', 'M', 'm')):
            break

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
    while True:
        print('Please choose the child the story should be personalized for: ')
        for ind in range(len(names)):
            print(f'{ind+1}. {names[ind]}')
        chosen = input('please select a number: \n')
        if validation.validate_num_input(chosen, len(names)):
            break

    ind = int(chosen) - 1
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
    print('The following stories are available: ')

    if child['sex'] == 'm':
        stories = list(config.male_stories.keys())
        while True:
            for ind in range(len(stories)):
                print(f'{ind+1}. {stories[ind]}')
            story_num = input('Please pick a number: \n')
            if validation.validate_num_input(story_num, len(stories)):
                break
        story_num = int(story_num)
        return config.male_stories[stories[story_num-1]]

    else:
        stories = list(config.female_stories.keys())
        while True:
            for ind in range(len(stories)):
                print(f'{ind+1}. {stories[ind]}')
            story_num = input('Please pick a number: \n')
            if validation.validate_num_input(story_num, len(stories)):
                break
        story_num = int(story_num)
        return config.female_stories[stories[story_num-1]]


def new_story() -> bool:
    """Let's the user choose if another story shoud be displayed

    Returns:
        bool: True if another story is required, False otherwise
    """
    while True:
        print('Do you wish to read another story?')
        new = input('Please enter yes\\no: \n')
        if validation.validate_str_select(new, ('YES', 'Yes', 'yes', 'NO', 'No', 'no')):
            break
    if new.upper() == 'YES':
        return True
    else:
        return False


def delete_child_option() -> bool:
    """Let's the user choose if child data should be deleted

    Returns:
        bool: True if data should be deleted, False otherwise
    """
    while True:
        print('Do you wish to delete your childs data?')
        delete = input('Please enter yes\\no: \n')
        if validation.validate_str_select(
                delete, ('YES', 'Yes', 'yes', 'NO', 'No', 'no')):
            break
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
    while True:
        print('Please choose the child you wish to delete: ')
        for ind in range(len(names)):
            print(f'{ind+1}. {names[ind]}')
        chosen = input('please select a number: \n')
        if validation.validate_num_input(chosen, len(names)-1):
            break

    del config.profiles[int(chosen)-1]

    return f'The child {names[int(chosen) - 1]} was successfully deleted'
