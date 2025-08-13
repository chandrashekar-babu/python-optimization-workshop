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
    

if __name__ == '__main__':
    while True:
        command = input("PyShell> ")
        args = command.split()
        if args[0] == "ls":
            list_dir(*args)
        elif args[0] == "pwd":
            show_path(*args)
        elif args[0] == "date":
            print_time(*args)
        elif args[0] == "exit":
            exit_shell(*args)
        else:
            invalid_command(*args)




