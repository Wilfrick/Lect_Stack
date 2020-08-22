from pathlib import Path



def new_course(name):
    current_directory = Path('.')
    course_directory = current_directory / name
    try:
        course_directory.mkdir()
    except FileExistsError:
        print("The directory already exists!")

    master_file = current_directory / name.title() + ".tex"
    try:
        master_file.touch()
    except FileExistsError:
        print("The master file already exists!")

    figures = course_directory / "figures"
    figures.mkdir()
    preamble = course_directory / "preamble.tex"
    preamble.touch()
    example_sheets = course_directory / "example_sheets"
    example_sheets.mkdir()

    # The body template assumes that the documentclass statement is in the default preamble.
    body = """\\input{{{0}/preamble.tex}}
\\title{{{1}.tex}}
\\begin{{document}}
\\maketitle
\\tableofcontents
% start lectures
% end lectures
\\end{{document}}
""".format(name, name.Title)
    master_file.write_text(body)