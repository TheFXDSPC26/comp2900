enterString = input('S to go to settings, E to exit, V to show program version, A to show about information: ')

while (enterString !='E'):

    if (enterString == 'S' or enterString == 's'):
            print(f'No settings to change')
            enterString = input('S to go to settings, E to exit, V to show program version, A to show about information: ')
    elif (enterString == 'E' or enterString == 'e'):
            print(f'Exiting program')   
    elif (enterString == 'V' or enterString == 'v'):
            print(f'Program version is 1.29.3')
            enterString = input('S to go to settings, E to exit, V to show program version, A to show about information: ')
    elif (enterString == 'A'):
            print(f'Sample program version 1.29.3 \nCopyright 2024 by Elliot Productions. \nAll rights reserved.')
            enterString = input('S to go to settings, E to exit, V to show program version, A to show about information: ')
    else:
            print('Invalid option selected')
            enterString = input('S to go to settings, E to exit, V to show program version, A to show about information: ')