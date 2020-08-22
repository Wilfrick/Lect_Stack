def get_file_contents_from_filepath_or_file_contents(filepath, file_contents_as_a_string = None):
    from pathlib import Path
    if type(filepath) == type(Path()):
        file_contents_as_a_string = filepath.read_text()
    elif type(filepath) == type(str()):
        with open(filepath, "rb") as f:
            file_contents_as_a_string = f.read()
    elif file_contents_as_a_string == None:
        raise RuntimeError("Filepath must be a file like object, or you must pass the file contents as a string")
    return file_contents_as_a_string

def get_header_footer(filepath, start_of_insertable_content_marker = "%start", end_of_insertable_content_marker = "%end", file_contents_as_a_string = None):
    part = 0
    header = ""
    footer = ""
    try:
        file_contents_as_a_string = get_file_contents_from_filepath_or_file_contents(filepath, file_contents_as_a_string)
    except RuntimeError as r:
        raise r
    finally:
        if file_contents_as_a_string == None:
            file_contents_as_a_string = ""
    for line in file_contents_as_a_string.spilt("\n"): # this should handle multiple instances of the markers well, but I don't think it does at the moment?
        if end_of_insertable_content_marker in line: # what does this even mean? I would suggest using re here
            part = 2
        if part == 0:
            header +=line
        if part == 2:
            footer +=line
        if start_of_insertable_content_marker in line: # what does this even mean? I would suggest using re here
            part = 1

    return header, footer

def replace_identifier_in_file_with_given_string(file_path, identifier, content_string, file_contents_as_a_string = None):
    identifier = "%succ"
    file_contents_as_a_string = "hi there\nHow are you\n%succ\nLol succ"
    print(get_header_footer(file_path, identifier, identifier, file_contents_as_a_string)) # needs doing


def Amalgamate_Files(path_to_output_file, sorted_list_of_filenames, template_path = None): # writes the combined file to the output path
    if template == None:
        with open(path_to_output_file, "wt") as f_out:
            for path in sorted_list_of_filenames:
                with open(path, "rt") as f_in:
                    file_Contents = f_in.read()
                    f_out.write(file_Contents)
    else: # use the template
        template_header, template_footer = get_header_footer(template_path)

