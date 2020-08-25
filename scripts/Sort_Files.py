def Sort_Filenames(list_of_file_paths, *args, **kwargs):
    sorted_list_of_file_paths = exclued_preamble_dot_tex(list_of_file_paths) # replace this with some actual logic
    return sorted_list_of_file_paths

def exclued_preamble_dot_tex(list_of_file_paths):
    return [file_path for file_path in list_of_file_paths if file_path.name != "preamble.tex"]