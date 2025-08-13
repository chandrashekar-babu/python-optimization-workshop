from command_dispatch import CommandDispatch

pyshell = CommandDispatch("PyShell> ")

@pyshell.for_command("ls")
def list_dir(*args):
    print("Listing directory of ", args)

@pyshell.for_command("pwd")
def show_path(*args):
    import os
    print(os.getcwd())

@pyshell.for_command("date")
def print_time(*args):
    from time import ctime
    print(ctime())

@pyshell.for_command("exit")
def exit_shell(*args):
    print("Exiting...")
    exit(0)

@pyshell.invalid
def invalid_command(*args):
    print("Invalid command -", args[0])
    
@pyshell.input
def getinput(prompt):
    return input(prompt).split()

if __name__ == '__main__':
    pyshell.run()
