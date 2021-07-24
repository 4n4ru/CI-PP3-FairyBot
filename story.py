import run
import config
import child_info
import textwrap as tr
import prompts
import user_input

def choose_child(profiles) -> int:
    """Prints a list of names to the console and lets the user pick one

    Args:
        profiles (list): a list containing all the child info dictionaries

    Returns:
        int: the index of the dictionary for the chosen child within the list
    """
    options = []
    for child in profiles:
        options.append(child.name)
    options.append('Add new child')
    chosen = user_input.pick_from_list(prompts.CHOOSE_CHILD, options)
    ind = options.index(chosen)
    return ind

def generate_story():
    while True:
        chosen = choose_child(config.profiles)
        while chosen == len(config.profiles):
            child = child_info.ChildInfo.add_child()
            config.profiles.insert(-1, child)
            chosen = choose_child(config.profiles)
        chosen_story = run.choose_story(config.profiles[chosen])
        story = run.generate_story(config.profiles[chosen], chosen_story)
        print(tr.fill(story, 70))
        
        if run.new_story():
            continue
        else:
            while run.delete_child_option() and len(config.profiles) > 0:
                if len(config.profiles) == 1:
                    print(prompts.NO_DELETE)
                    break
                else:
                    print(run.delete_child(config.profiles))
            break

generate_story()