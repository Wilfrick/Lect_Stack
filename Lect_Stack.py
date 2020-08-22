

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
            from scripts.













if __name__ == "__main__":
    main()