from pathlib import Path

def newCourse(name):
    currentDirectory = Path('.')
    courseDirectory = currentDirectory / name
    try:
        courseDirectory.mkdir()
    except FileExistsError:
        print("The directory already exists!")

    masterFile = currentDirectory / name + ".tex"
    try:
        masterFile.mkdir()
    except FileExistsError:
        print("The master file already exists!")
