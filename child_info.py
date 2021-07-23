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

    def make_dictionary(self) -> dict:
        """Makes a dictionary from the child info

        Returns:
            dict: dictionary with child info
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
