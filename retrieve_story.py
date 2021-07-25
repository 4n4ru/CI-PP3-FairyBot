import user_input
import prompts
import csv

def retrieve_story_option() -> bool:
    """Ask user if a saved stroy should be retrieved and saves user input into 
    the retrieve variable. If the answer is yes, return true, false otherwise

    Returns:
        bool: True if a saved story should be retrieved, False otherwise
    """
    retrieve = user_input.select_input(
        prompts.RETRIEVE_OPTION, prompts.YES_NO_OPTIONS)
    if retrieve.upper() == 'YES':
        return True
    else:
        return False

def retrieve_story():
    """Promts user to input user id and prints story.
    Calls a function to ask the user if a story should be retrieved. If it
    should, reads from the csv file and appends all rows to stories list. Asks 
    the user for the user id until a correct user id is given. Once a correct 
    one is give, save the story in the story variable and print it to the
    terminal
    """
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
        
