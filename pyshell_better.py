def list_dir(*args):
    print("Listing directory of ", args)

def show_path(*args):
    import os
    print(os.getcwd())

def print_time(*args):
    from time import ctime
    print(ctime())

def exit_shell(*args):
    print("Exiting...")
    exit(0)

def invalid_command(*args):
    print("Invalid command -", args[0])
    

commands = {
    "ls": list_dir,
    "date": print_time,
    "pwd": show_path,
    "exit": exit_shell
}

if __name__ == '__main__':
    while True:
        command = input("PyShell> ")
        args = command.split()
        commands.get(args[0], invalid_command)(*args)




