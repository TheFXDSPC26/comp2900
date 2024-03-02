enterCommand = ''
started = ""
while True:
                enterCommand = input('\n\nType command: ').lower()
                if enterCommand == 'help':
                        enterCommand = print('\n\nStart - start car\n\nStop - stop car\n\nQuit - quit program\n\n')
                elif enterCommand == 'start':
                        if started != True:
                                started = True
                                print('Car started!')
                        elif started == True:
                                print('Car has been already started!')
                elif enterCommand == 'stop':
                        if started == True:
                                started = False
                                print('Car stopped!')
                        elif started == False:
                                print('Car has been already stopped!')
                elif enterCommand == 'quit':
                        print('Closing program')
                        break
                else:
                        print("I don't undestand that")              