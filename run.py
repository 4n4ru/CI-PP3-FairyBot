import textwrap as tr
import config


class ChildInfo:
    """
    Child info class
    """

    def __init__(self,
                 name, friend, color, food, animal, sport, disliked_food, sex):
        # instance attribute
        self.name = name
        self.friend = friend
        self.color = color
        self.food = food
        self.animal = animal
        self.sport = sport
        self.disliked_food = disliked_food
        self.sex = sex

    def make_dictionary(self):
        """
        Creates a dictionary with child info
        returns: dictionary
        """
        child_dict = {
            'name': self.name,
            'friend': self.friend,
            'color': self.color,
            'food': self.food,
            'animal': self.animal,
            'sport': self.sport,
            'disliked-food': self.disliked_food,
            'sex': self.sex
        }
        return child_dict


def pick_color():
    """
    Gets user input for favorite color
    returns string
    """
    while True:
        print('Please choose your childs favorite colour:')
        print('1. Blue')
        print('2. Pink')
        print('3. Yellow')
        print('4. Orange')
        color = input('Enter a number: \n')
        if validate_num_input(color, 4):
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


def validate_num_input(user_input, max_num):
    try:
        num = int(user_input)
        if num < 1 or num > max_num:
            raise ValueError(
                f'This should be a number between 1 and {max_num}!')
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False
    return True


def add_child():
    """
    Gets user input for child info
    returns child dictionary
    """
    while True:
        name = input('Please enter your childs name:\n').capitalize()
        if validate_str_input(name):
            break

    while True:        
        friend = input(
            'Please enter your childs best friends name:\n').capitalize()
        if validate_str_input(friend):
            break

    color = pick_color()

    while True:
        food = input('Please enter your childs favourite food:\n')
        if validate_str_input(food):
            break

    while True:
        animal = input('Please enter your childs favourite animal: \n')
        if validate_str_input(animal):
            break

    while True:
        sport = input('Please enter your childs favourite team sport: \n')
        if validate_str_input(sport):
            break

    while True:
        disliked_food = input('Please enter a food your child dislikes: \n')
        if validate_str_input(disliked_food):
            break
    while True:
        sex = input('Is your child male or female? Please enter f\\m: \n')
        if validate_str_select(sex, ('F', 'f', 'M', 'm')):
            break

    child = ChildInfo(
        name, friend, color, food, animal, sport, disliked_food, sex)
    return child.make_dictionary()


def validate_str_input(user_input):
    if (not user_input.isalpha()) or len(user_input) < 2:
        print(
            'Your input should be a single word of a minimum of 2 characters.'
            'Please try again.')
        return False
    return True


def validate_str_select(sex, answer_set):
    if sex not in answer_set:
        print('Invalid input. Please try again.')
        return False
    return True


def choose_child(profiles):
    """
    Ask user to choose a child from the list of childrens names
    returns index of chosen option
    """
    names = []
    for child in profiles:
        names.append(child['name'])
    while True:
        print('Please choose the child the story should be personalized for: ')
        for ind in range(len(names)):
            print(f'{ind+1}. {names[ind]}')
        chosen = input('please select a number: \n')
        if validate_num_input(chosen, len(names)):
            break

    ind = int(chosen) - 1
    return ind


def generate_story(child, story):
    """
    Generates the custom story using a dictionary with child info by replacing
    placeholder text
    returns custom story
    """
    with open(story) as f:
        story = f.read()
    custom_story = story.format(**child)
    return custom_story


def choose_story(child):
    """
    Prints out a list of available stories
    Retruns file path of selected story
    """
    print('The following stories are available: ')

    if child['sex'] == 'm':
        stories = list(config.male_stories.keys())
        while True:
            for ind in range(len(stories)):
                print(f'{ind+1}. {stories[ind]}')
            story_num = input('Please pick a number: \n')
            if validate_num_input(story_num, len(stories)):
                break
        story_num = int(story_num)
        return config.male_stories[stories[story_num-1]]

    else:
        stories = list(config.female_stories.keys())
        while True:
            for ind in range(len(stories)):
                print(f'{ind+1}. {stories[ind]}')
            story_num = input('Please pick a number: \n')
            if validate_num_input(story_num, len(stories)):
                break
        story_num = int(story_num)
        return config.female_stories[stories[story_num-1]]


def new_story():
    while True:
        print('Do you wish to read another story?')
        new = input('Please enter yes\\no: \n')
        if validate_str_select(new, ('YES', 'Yes', 'yes', 'NO', 'No', 'no' )):
            break
    if new.upper() == 'YES':
        return True
    else:
        return False

def delete_child_option():
    while True:
        print('Do you wish to delete your childs data?')
        delete = input('Please enter yes\\no: \n')
        if validate_str_select(delete, ('YES', 'Yes', 'yes', 'NO', 'No', 'no' )):
            break
    if delete.upper() == 'YES':
        return True
    else:
        return False



def main():
    print('Welcome to Fairy Bot!\n')
    profiles = [{'name': 'Add new child'}]
    while True:
        if len(profiles) == 1:
            child = add_child()
            profiles.insert(-1, child)
        chosen = choose_child(profiles)
        while profiles[chosen]['name'] == 'Add new child':
            child = add_child()
            profiles.insert(-1, child)
            chosen = choose_child(profiles)
        chosen_story = choose_story(profiles[chosen])
        story = generate_story(profiles[chosen], chosen_story)
        print(tr.fill(story, 70))
        if new_story():
            continue
        else:
            if delete_child_option():
                pass
            break

main()
