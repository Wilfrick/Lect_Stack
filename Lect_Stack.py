

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
        if len(options) > 0:
            pass # add more logic here to deal with other options
        else: # default behaviour
            from os import getcwd, path # rewrite this to use pathlib at some point
            path_to_directory = path.join(getcwd(), argv[-1])
            if not path.isdir(path_to_directory):
                show_help()
                print("This failed because the path provided was not a directory") # this might still fail for special links, needs testing
            from scripts.Enumerate_Files import Enumerate_Filenames
            from scripts.Amalgamate_Files import Amalgamate_Files
            from scripts.Sort_Files import Sort_Filenames
            from pathlib import Path

            list_of_file_paths = Enumerate_Filenames(Path(path_to_directory)) # when this all gets rewritten to use pathlib.Path by default this line can be simplified
            sorted_list_of_file_paths = Sort_Filenames(list_of_file_paths, sort = "number")
            Amalgamate_Files(Path(path_to_directory).joinpath("..\\{}.tex".format(Path(argv[-1]).name)).resolve(), sorted_list_of_file_paths, Path(path_to_directory).joinpath("..\\default_template.tex").resolve()) # fill in these arguments

            print("Success")
            exit(0)













if __name__ == "__main__":
    main()