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

def write_file_contents_to_file(file_path, file_contents_as_a_string):
    from pathlib import Path
    if type(file_path) == type(Path()):
        file_path.write_text(file_contents_as_a_string)
    if type(file_path) == type(str()):
        with open(file_path, "wt") as f:
            amount_of_content = len(file_contents_as_a_string)
            amount_of_content_that_was_written = f.write(file_contents_as_a_string)
            if amount_of_content != amount_of_content_that_was_written:
                print("Mismatch in write_file_contents_to_file, but hopefully everything is fine")

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


def Amalgamate_Files(path_to_output_file, sorted_list_of_file_paths, template_path = None, source_directory_name = None, local_images_directory_name = "figures", local_premable_file_name = "preamble.tex"): # writes the combined file to the output path
    if source_directory_name == None:
        source_directory_name = path_to_output_file.name[:-4]
    if template_path == None:
        with open(path_to_output_file, "wt") as f_out:
            for path in sorted_list_of_file_paths:
                with open(path, "rt") as f_in:
                    file_Contents = f_in.read()
                    f_out.write(file_Contents)
    else: # use the template
        template_file_contents_as_a_string = get_file_contents_from_filepath_or_file_contents(template_path)
        lookup_dictionary = {r"##ENTRIES##": "\n".join(r"\input{{{}}}".format(str(file_path).replace("\\", "/")) for file_path in sorted_list_of_file_paths),
                             r"##AUTHOR##": "Henry",
                             r"##TITLE##": path_to_output_file.name,
                             r"##PATH_TO_IMAGE_FOLDER##": str(path_to_output_file.parent / source_directory_name / local_images_directory_name).replace("\\", "/"),
                             r"##PATH_TO_LOCAL_PREAMBLE##": str(path_to_output_file.parent / source_directory_name / local_premable_file_name).replace("\\", "/")}
        output_file_contents = replace_identifiers_with_lookup_dictionary_in_string(template_file_contents_as_a_string, lookup_dictionary)
        write_file_contents_to_file(path_to_output_file, output_file_contents)


