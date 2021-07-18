class ChildInfo:
    """
    Child info class
    """

    def __init__(self, name, parent, friend, hair, eyes):
        # instance attribute
        self.name = name
        self.parent = parent
        self.friend = friend
        self.hair = hair
        self.eyes = eyes

    def make_dictionary(self):
        """
        Creates a dictionary with child info
        returns: dictionary
        """
        child_dict = {
            'name': self.name,
            'parent': self.parent,
            'friend': self.friend,
            'hair': self.hair,
            'eyes': self.eyes
        }
        return child_dict


def pick_eye_color():
    """
    Gets user input for eye color
    returns string
    """
    while True:
        print('Please choose your childs eye colour:')
        print('1. Black')
        print('2. Brown')
        print('3. Green')
        print('4. Blue')
        try:
            eye_color = int(input())
            if eye_color < 1 or eye_color > 4:
                raise ValueError('This should be a number between 1 and 4!')
            else:
                break
        except ValueError as e:
            print(f'Invalid data: {e}, please try again.\n')
    if eye_color == 1:
        return 'black'
    elif eye_color == 2:
        return 'brown'
    elif eye_color == 3:
        return 'green'
    else:
        return 'blue'


def pick_hair_color():
    """
    Gets user input for hair color
    returns string
    """
    while True:
        print('Please choose your childs hair colour:')
        print('1. Black')
        print('2. Brown')
        print('3. Blond')
        try:
            eye_color = int(input())
            if eye_color < 1 or eye_color > 3:
                raise ValueError('This should be a number between 1 and 4!')
            else:
                break
        except ValueError as e:
            print(f'Invalid data: {e}, please try again.\n')
    if eye_color == 1:
        return 'black'
    elif eye_color == 2:
        return 'brown'
    else:
        return 'blond'


def add_child():
    """
    Gets user input for child info
    returns child dictionary
    """
    name = input('Please enter your childs name:\n')
    parent = input('Please enter the childs parents name:\n')
    friend = input('Please enter your childs best friends name:\n')
    hair = pick_hair_color()
    eyes = pick_eye_color()
    child = ChildInfo(name, parent, friend, hair, eyes)
    return child.make_dictionary()


def main():
    print('Welcome to Fairy Bot!\n')
    profiles = []
    child = add_child()
    profiles.append(child)
    print(profiles)


main()
