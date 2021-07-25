def main():
    """imports module for welcome message, retrieveing saved story, creating 
    the story and end message

    Raises:
        ImportError: if the welcome module fails to import
        ImportError: if the retrieve_story module fails to import
        ImportError: if the story module fails to import
        ImportError: if the end module fails to import
    """
    try:
        import welcome
    except ImportError:
        raise ImportError('welcome module failed to import')

    try:
        import retrieve_story
    except ImportError:
        raise ImportError('retrieve_story module failed to import')

    try:
        import story
    except ImportError:
        raise ImportError('story module failed to import')
    
    try:
        import end
    except ImportError:
        raise ImportError('end module failed to import')

if __name__ == "__main__":
    main()
