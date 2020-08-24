

def main():
    from sys import argv, exit


    number_of_arguments = len(argv)
    def show_help():
        print(
"""Usage is: python3 Lect_Stack.py [<options>] <directory>
Options:
    -h      show this help""")

    options = {}
    if number_of_arguments == 1 or argv[0] == "-c": # incorrect usage
        show_help()
        exit(0)
    elif number_of_arguments > 2: # we have some options set
        if argv[1] == "-h":
            show_help()
            exit(0)
    else: # standard usage
        if len(options) >= 0:
            pass # add more logic here to deal with other options
        else: # default behaviour
            from os import getcwd, path
            path_to_directory = path.join(argv[-1], getcwd)
            if not os.path.isdir(path_to_directory):
                show_help()
                print("This failed because the path provided was not a directory") # this might still fail for special links, needs testing
            from scripts.Enumerate_Files import Enumerate_Filenames
            from scripts.Amalgamate_Files import Amalgamate_Files
            from scripts.Sort_Files import Sort_Files
            list_of_files = Enumerate_Filenames(path_to_directory)
            sorted_list_of_files = Sort_Files(list_of_files)
            Amalgamate_Files() # fill in these arguments














if __name__ == "__main__":
    main()