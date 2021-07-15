from cx_Freeze import setup, Executable

base = None    

executables = [Executable("listecourse.py", base=base)]

packages = ["idna", "pyfiglet"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<test>",
    options = options,
    version = "<0.1>",
    description = '<Liste de courses>',
    executables = executables
)
