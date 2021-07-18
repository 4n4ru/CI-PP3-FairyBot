class ChildInfo:
    """
    Child info class
    """

    def __init__(self, name, friend, color, food):
        # instance attribute
        self.name = name
        self.friend = friend
        self.color = color
        self.food = food

    def make_dictionary(self):
        """
        Creates a dictionary with child info
        returns: dictionary
        """
        child_dict = {
            'name': self.name,
            'friend': self.friend,
            'color': self.color,
            'food': self.food
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
            color = int(input())
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


# def pick_hair_color():
#     """
#     Gets user input for hair color
#     returns string
#     """
#     while True:
#         print('Please choose your childs hair colour:')
#         print('1. Black')
#         print('2. Brown')
#         print('3. Blond')
#         try:
#             eye_color = int(input())
#             if eye_color < 1 or eye_color > 3:
#                 raise ValueError('This should be a number between 1 and 4!')
#             else:
#                 break
#         except ValueError as e:
#             print(f'Invalid data: {e}, please try again.\n')
#     if eye_color == 1:
#         return 'black'
#     elif eye_color == 2:
#         return 'brown'
#     else:
#         return 'blond'


def add_child():
    """
    Gets user input for child info
    returns child dictionary
    """
    name = input('Please enter your childs name:\n')
    friend = input('Please enter your childs best friends name:\n')
    color = pick_color()
    food = input('Please enter your childs favourite food:\n')
    child = ChildInfo(name, friend, color, food)
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
            chosen = int(input('Please select one: \n'))
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
    with open('stories/a-golden-touch.txt') as f:
        story = f.read()
    custom_story = story.format(**child)
    return custom_story


def main():
    print('Welcome to Fairy Bot!\n')
    profiles = [{'name': 'Add new child'}]
    chosen = choose_child(profiles)
    if profiles[chosen]['name'] == 'Add new child':
        child = add_child()
        profiles.insert(-2, child)
        chosen = choose_child(profiles)
    story = generate_story(profiles[chosen])
    print(story)


main()
