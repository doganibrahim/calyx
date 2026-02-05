import sys
def main():
    builtinList = ['exit', 'echo', 'type']
    while True:
        sys.stdout.write("$ ")
        command = input()
        if not command:
            continue
        if command == "exit":
            break
        if command.split()[0] == "echo":
            print(command[5:])
        elif command.split()[0] == "type":
            if command.split()[1] in builtinList:
                print(f'{command.split()[1]} is a shell builtin')
            else:
                print(f'{command.split()[1]}: not found')
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()