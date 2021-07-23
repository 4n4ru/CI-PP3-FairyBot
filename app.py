import textwrap as tr

def main():
    import run
    import config

    print('Welcome to Fairy Bot!\n')
    print(config.ascii_book)
    print('\n')

    while True:
        if len(config.profiles) == 1:
            child = run.add_child()
            config.profiles.insert(-1, child)
        chosen = run.choose_child(config.profiles)
        while config.profiles[chosen]['name'] == 'Add new child':
            child = run.add_child()
            config.profiles.insert(-1, child)
            chosen = run.choose_child(config.profiles)
        chosen_story = run.choose_story(config.profiles[chosen])
        story = run.generate_story(config.profiles[chosen], chosen_story)
        print(tr.fill(story, 70))
        
        if run.new_story():
            continue
        else:
            while run.delete_child_option() and len(config.profiles) > 0:
                if len(config.profiles) == 1:
                    print('There are no more children to delete.')
                    break
                else:
                    print(run.delete_child(config.profiles))
            break

    print('Thank you for using the Fairy Bot app. If you want to restart it'
        'press the Run Fairy Bot button.')



main()
