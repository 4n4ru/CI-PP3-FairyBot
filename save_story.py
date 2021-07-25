import user_input
import prompts
import shortuuid
import csv

def save_story_option():
    save = user_input.select_input(prompts.SAVE_OPTION, prompts.YES_NO_OPTIONS)
    if save.upper() == 'YES':
        return True
    else:
        return False

def save_story(story):
    save = save_story_option()
    if save:
        user_id = shortuuid.uuid()[:7]
        row = [user_id, story]
        with open('stories/saved-stories.csv', 'a') as f:
            w = csv.writer(f)
            w.writerow(row)
    
    return user_id
