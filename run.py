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


def main():
    print('Welcome to Fairy Bot!\n')


main()
