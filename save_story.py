import user_input
import prompts
import shortuuid

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
        print(user_id)
        dict = {user_id: story}
        with open('stories/saved-stories.csv', 'w') as f:
            f.write(f'{dict}')
