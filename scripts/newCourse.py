from pathlib import Path


def newCourse(name):
    current_directory = Path('.')
    course_directory = current_directory / name
    try:
        course_directory.mkdir()
    except FileExistsError:
        print("The directory already exists!")

    master_file = current_directory / name + ".tex"
    try:
        master_file.touch()
    except FileExistsError:
        print("The master file already exists!")
