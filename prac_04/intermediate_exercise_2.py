def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    valid_username = False
    while not valid_username:
        user_input = input("Please enter your username to gain access: ")
        if user_input in usernames:
            print("Access Granted")
            valid_username = True
        else:
            print("Access Denied")


main()
