import prompts
import user_input

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

    @staticmethod
    def add_child() -> dict:
        """Creates a child dictionary by calling different functions for user input

        Returns:
            dict: info about the child
        """
        name = user_input.input_string(prompts.ENTER_NAME).capitalize()
        friend = user_input.input_string(prompts.ENTER_FRIEND).capitalize()
        color = user_input.pick_from_list(prompts.ENTER_COLOR, prompts.COLORS)
        food = user_input.input_string(prompts.ENTER_FOOD)
        animal = user_input.input_string(prompts.ENTER_ANIMAL)
        sport = user_input.input_string(prompts.ENTER_SPORT)
        disliked_food = user_input.input_string(prompts.ENTER_DISLIKED_FOOD)
        sex = user_input.select_input(prompts.ENTER_SEX, prompts.SEX_OPTIONS)
        
        child = ChildInfo(
            name, friend, color, food, animal, sport, disliked_food, sex)
        return child
