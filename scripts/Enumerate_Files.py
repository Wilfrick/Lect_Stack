def Enumerate_Filenames(full_path_to_directory, file_extensions = [".tex"]):
    list_of_files_in_path = [path for path in full_path_to_directory.iterdir() if path.is_file()]
    for file in list_of_files_in_path:
        print(file.name)
    return list_of_files_in_path

