import user_input
import prompts
import shortuuid
import csv

def save_story_option() -> bool:
    """Asks the user if the last generated story should be saved for later

    Returns:
        bool: true if the story should be saved, false otherwise
    """
    save = user_input.select_input(prompts.SAVE_OPTION, prompts.YES_NO_OPTIONS)
    if save.upper() == 'YES':
        return True
    else:
        return False

def save_story(story) -> str:
    """Saves story to csv file.
    Generates a user_id, creates a list with user_id and story as elements and
    appends the list to the next row in the csv file

    Args:
        story (str): The last story generated passed as an argument

    Returns:
        str: user id
    """
    # code form https://github.com/skorokithakis/shortuuid
    user_id = shortuuid.uuid()[:7]
    # code from https://stackoverflow.com/a/37654233
    row = [user_id, story]
    with open('stories/saved-stories.csv', 'a') as f:
        w = csv.writer(f)
        w.writerow(row)
    
    return user_id
