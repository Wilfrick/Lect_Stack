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


def define_custom_template_class(new_id_pattern = r"\#\#[_a-z][_a-z0-9]{1,}?\#\#", new_brace_id_pattern = None, new_delimiter = r""):
    from string import Template
    class Custom_Template(Template):
        delimiter = new_delimiter
        idpattern = new_id_pattern
        braceidpattern = new_brace_id_pattern
        pass
    return Custom_Template


def replace_identifiers_with_lookup_dictionary_in_string(template_string, lookup_dictionary, template_class = define_custom_template_class()):
    replacement_codepoints = {"{": chr(0xF007B), "}": chr(0xF007D)}
    custom_template_object = template_class(template_string.replace("{", replacement_codepoints["{"]).replace("}", replacement_codepoints["}"])) # transpose "{" and "}" so they won't affect the template code
    template_string_with_new_insertions = custom_template_object.safe_substitute(lookup_dictionary).replace(replacement_codepoints["{"], "{").replace(replacement_codepoints["}"], "}")
    return template_string_with_new_insertions


def Amalgamate_Files(path_to_output_file, sorted_list_of_filenames, template_path = None): # writes the combined file to the output path
    if template == None:
        with open(path_to_output_file, "wt") as f_out:
            for path in sorted_list_of_filenames:
                with open(path, "rt") as f_in:
                    file_Contents = f_in.read()
                    f_out.write(file_Contents)
    else: # use the template
        template_file_contents_as_a_string = get_file_contents_from_filepath_or_file_contents(template_path)
        from string import Template


