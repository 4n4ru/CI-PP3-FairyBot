import textwrap as tr


class ChildInfo:
    """
    Child info class
    """

    def __init__(self,
                 name, friend, color, food, animal, sport, dislike_food, sex):
        # instance attribute
        self.name = name
        self.friend = friend
        self.color = color
        self.food = food
        self.animal = animal
        self.sport = sport
        self.dislike_food = dislike_food
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
            'dislike_food': self.dislike_food,
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
        print('2. Green')
        print('3. Pink')
        print('4. Yellow')
        print('5. Orange')
        print('6. Red')
        print('7. Purple')
        try:
            color = int(input('Enter a number: \n'))
            if color < 1 or color > 7:
                raise ValueError('This should be a number between 1 and 7!')
            else:
                break
        except ValueError as e:
            print(f'Invalid data: {e}, please try again.\n')
    if color == 1:
        return 'blue'
    elif color == 2:
        return 'green'
    elif color == 3:
        return 'pink'
    elif color == 4:
        return 'yellow'
    elif color == 5:
        return 'orange'
    elif color == 6:
        return 'red'
    else:
        return 'purple'


def add_child():
    """
    Gets user input for child info
    returns child dictionary
    """
    name = input('Please enter your childs name:\n')
    friend = input('Please enter your childs best friends name:\n')
    color = pick_color()
    food = input('Please enter your childs favourite food:\n')
    animal = input('Please enter your childs favourite animal: \n')
    sport = input('Please enter your childs favourite team sport: \n')
    dislike_food = input('Please enter a food your child dislikes: \n')
    sex = input('Is your child male or female? Please enter f/m: \n')
    child = ChildInfo(
        name, friend, color, food, animal, sport, dislike_food, sex)
    return child.make_dictionary()


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
        try:
            chosen = int(input('Please select a number: \n'))
            if chosen < 1 or chosen > len(names):
                raise ValueError(
                    f'This should be a number between 1 and {len(names)}!')
            else:
                break
        except ValueError as e:
            print(f'Invalid data: {e}, please try again.\n')
    return chosen - 1


def generate_story(child):
    """
    Generates the custom story using a dictionary with child info by replacing
    placeholder text
    returns custom story
    """
    with open('stories/male-main-character/a-golden-touch.txt') as f:
        story = f.read()
    custom_story = story.format(**child)
    return custom_story


def main():
    print('Welcome to Fairy Bot!\n')
    profiles = [{'name': 'Add new child'}]
    if len(profiles) == 1:
        child = add_child()
        profiles.insert(-1, child)
    chosen = choose_child(profiles)
    while profiles[chosen]['name'] == 'Add new child':
        child = add_child()
        profiles.insert(-1, child)
        chosen = choose_child(profiles)
    story = generate_story(profiles[chosen])
    print(tr.fill(story, 70))


main()
