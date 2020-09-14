import re

def Sort_Filenames(list_of_file_paths, *args, **kwargs):
    preambless_file_paths = exclued_preamble_dot_tex(list_of_file_paths) 
    sorting_method = get_sorting_method(args,kwargs)

    if sorting_method == "number":
        sorted_list_of_file_paths = sort_by_number(preambless_file_paths)
    else:
        sorted_list_of_file_paths = preambless_file_paths
     
    return sorted_list_of_file_paths

def exclued_preamble_dot_tex(list_of_file_paths):
    return [file_path for file_path in list_of_file_paths if file_path.name != "preamble.tex"]

def get_sorting_method(args,kwargs,valid_sorting_methods = ["number", "alphabetical"]): # define reasonable default for valid_sorting_methods
    # count the number of sorting arguments
    arg_num = 0
    arg_list = []
    for arg in args:
        if arg in valid_sorting_methods:
            arg_num += 1
            arg_list.append(arg)
    for key in kwargs.keys():
        if key == "sort":
            if kwargs[key] in valid_sorting_methods:
                arg_num += 1
                arg_list.append(kwargs[key])
            else:
                raise RuntimeError("The sorting method is not valid!")
    # verify that there is exactly one sorting argument
    if arg_num == 0:
        raise RuntimeError("No valid sorting methods provided!")
    elif arg_num > 1:
        raise RuntimeError("Too many sorting methods provided, please decide on one!")
    elif arg_num == 1:
        return args[0]
    else:
        raise RuntimeError("You broke the program and my brain, congrats!")

def make_number_file_dictionary(list_of_file_paths):
    number_file_dictionary = {}
    for path in list_of_file_paths:
        try:
            number_file_dictionary[int(re.findall(r'\d+',str(path))[-1])] = path
        except IndexError:
            print("Couldn't find a number for the file called: " + str(path))
    return number_file_dictionary

def sort_by_number(list_of_file_paths):
    number_file_dictionary = make_number_file_dictionary(list_of_file_paths)
    sorted_numbers = sorted(number_file_dictionary.keys())
    sorted_by_number = [number_file_dictionary[number] for number in sorted_numbers]
    return sorted_by_number