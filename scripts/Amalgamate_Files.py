def get_header_footer(filepath, start_of_insertable_content_marker = "%start", end_of_insertable_content_marker = "%end", file_contents_as_a_string = None):
    part = 0
    header = ""
    footer = ""
    from pathlib import Path
    if type(filepath) == type(Path()):
        file_contents_as_a_string = filepath.read_text()
    elif type(filepath) == type(str()):
        with open(filepath, "rb") as f:
            file_contents_as_a_string = f.read()
    elif file_contents_as_a_string == None:
        raise RuntimeError("Filepath must be a file like object, or you must pass the file contents as a string")
    for line in file_contents_as_a_string.spilt("\n"):
        if end_of_insertable_content_marker in line:
            part = 2
        if part == 0:
            header +=line
        if part == 2:
            footer +=line
        if start_of_insertable_content_marker in line:
            part = 1

    return header, footer


def Amalgamate_Files(path_to_output_file, sorted_list_of_filenames, template = None): # writes the combined file to the output path
    if template == None:
        with open(path_to_output_file, "wt") as f_out:
            for path in sorted_list_of_filenames:
                with open(path, "rt") as f_in:
                    file_Contents = f_in.read()
                    f_out.write(file_Contents)
    else: # use the template
        template_header, template_footer = get_header_footer(template)

