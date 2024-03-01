print('Welcome to the Car Game! Type help for a list of commands to get started: ')
i = 0
while i<999:
    z=1
    y=2
    c=0    
    enterCommand = input('Type choice\n\n(Input) to type or (help) for list of commands: ')
    if enterCommand == 'help':      
            commandProgram = input('Start - start car\n\nStop - stop car\n\nQuit - quit program: ')
            commandProgram = commandProgram.upper()
            if commandProgram == 'START':
                    i = z
            elif commandProgram == 'STOP':
                    i = y
            else:
                    i = c
            if i == 1:
                    print('Car started!')
            elif i == 2:
                    print('Car stopped!')
            else:
                print('Closing program')
                exit()
    else:
            commandProgram = input('> ')
            commandProgram = commandProgram.upper()
            if commandProgram == 'START':
                    i = z
            elif commandProgram == 'STOP':
                    i = y
            else:
                    i = c
            if i == 1:
                    print('Car started!')
            elif i == 2:
                    print('Car stopped!')
            else:
                print('Closing program')
                exit()