"""
Complete this program to implement the rudimentary
interactive command shell. Implement the run()
function below and make necessary changes to
ensure that the shell works as per the transcript
shown below:
----------------------------------------------------
    $ python pyshell.py
    PyShell> list /bin /usr /opt
    Listing contents of ("/bin", "/usr", "/opt")

    PyShell> date
    Tue Aug 01 09:30:00 2017

    PyShell> dslfjsdfdsf
    Invalid command - dslfjsdfdsf

    PyShell> exit
    $
------------------------------------------------------
Implement a scalable solution; i.e., adding new commands
must be mostly effortless and the shell command evaluation
must be performance efficient.

[ Download stub code from https://files.chandrashekar.info/pyshell_exercise.py ]

"""

# Invoke this function if the command is 'list'
def list_directory(*args):
    from os import listdir
    if len(args) < 2:
        args += ".",
    for path in args[1:]:
        print("{}:".format(path))
        print("\n".join(listdir(path)))

# Invoke this function if the command is 'whoami'
def show_user(*args):
    from getpass import getuser
    print(getuser())

# Invoke this function if the command is 'date'
def print_date(*args):
    from time import ctime
    print(ctime())

# Invoke this function if the command is 'exit'
def exit_shell(*args):
    exit(0)

# Invoke this function if the command is anything else
def invalid_command(*args):
    print("Invalid command - ", args[0])


def run():
    while True:
        command = input("PyShell> ")
        pass # TODO: Implement the logic here!


if __name__ == '__main__':
    run()