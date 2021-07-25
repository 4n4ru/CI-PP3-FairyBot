import user_input
import prompts
import csv

def retrieve_story_option():
    retrieve = user_input.select_input(
        prompts.RETRIEVE_OPTION, prompts.YES_NO_OPTIONS)
    if retrieve.upper() == 'YES':
        return True
    else:
        return False

def retrieve_story():
    while True:
        retrieve = retrieve_story_option()
        if retrieve == False:
            break

        stories = []
        with open('stories/saved-stories.csv', 'r') as f:
            r = csv.reader(f)
            for row in r:
                stories.append(row)

        while True:
            user_id_found = False
            user_id = input(prompts.ENTER_USER_ID)
            for ind in range(len(stories)):
                if stories[ind][0] == user_id:
                    user_id_found = True
            if user_id_found == True:
                story = stories[ind][1]
                break
        
        print(story)

retrieve_story()
        
