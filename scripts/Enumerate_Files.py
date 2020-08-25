def Enumerate_Filenames(full_path_to_directory, file_extensions = [".tex"]):
    from pathlib import Path
    list_of_files_in_path = [path for path in Path(full_path_to_directory).iterdir() if path.is_file() and path.name[-4:] == ".tex"]
    return list_of_files_in_path

