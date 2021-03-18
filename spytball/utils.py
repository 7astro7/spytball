
def get_directory_name(a_directory: str):
    """
    """
    print(type(a_directory))
    if not args.get("directory-name"):
        # IF NO DEFAULT DIRS SET 
        print("we here")
        print("no directory or file chosen")
        sys.exit(1)
    # IF DEFAULT DIR IS SET, collect THAT DIR 
    dir_name = args.get("directory-name")
    if not os.path.exists(dir_name):
        print("Directory not found in file system")
        sys.exit(1)
    return dir_name



def configure():
    """
    Modify defaults
    """
    pass

def is_viable_user():
    """
    Return true if user has gpg privileges
    """
    pass

def simulate_a_spytball():
    """
    Create example 
    """
    pass