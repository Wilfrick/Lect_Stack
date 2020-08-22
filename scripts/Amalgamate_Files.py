def Amalgamate_Files(path_to_output_file, sorted_list_of_filenames, template = None): # writes the combined file to the output path
    if template == None:
        with open(path_to_output_file, "wt") as f_out:
        for path in sorted_list_of_filenames:
            with open(path, "rt") as f_in:
                file_Contents = f_in.read()
                f_out.write(file_Contents)

