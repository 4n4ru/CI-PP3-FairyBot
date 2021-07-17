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


def add_child():
    """
    Gets user input for child info
    returns child
    """
    name = input('Please enter your childs name:\n')
    parent = input('Please enter the childs parents name:\n')
    friend = input('Please enter your childs best friends name:\n')
    hair = pick_hair_color()
    eyes = pick_eye_color()
    child = ChildInfo.child_dict(name, parent, friend, hair, eyes)
    return child


def main():
    print('Welcome to Fairy Bot!\n')
    child = add_child()

main()
