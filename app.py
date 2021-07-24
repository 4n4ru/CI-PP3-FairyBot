import textwrap as tr
import prompts

def main():
    import child_info
    import config
    import run

    print(prompts.WELCOME)
    print(config.ascii_book)
    print('\n')

    while True:
        chosen = run.choose_child(config.profiles)
        while config.profiles[chosen]['name'] == 'Add new child':
            child = child_info.ChildInfo.add_child()
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
                    print(prompts.NO_DELETE)
                    break
                else:
                    print(run.delete_child(config.profiles))
            break

    print(prompts.THANK_YOU)

if __name__ == "__main__":
    main()
