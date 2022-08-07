# Run Keyboard

import Keyboard

if __name__ == '__main__':
    keys = Keyboard.Keyboard()
    filePath = str(input('Enter file location: '))
    out = ''
    with open(filePath, 'r') as file:
        params = str(file.read()).split('\n') #should be baseURL, gameId -- as of 8/3/22 baseURL is set in grabESPNNFL
        print(params)
        numGames = str(input('How many games? '))
        run = False
        if len(params) == 2:
            keys.grabESPNNFL(params[1], int(numGames))
            run = True
        if run:
            params[1] = str(int(params[1]) - int(numGames))
        out = str(params[0]) + '\nstr' + str(params[1])

    with open(filePath, 'w'):
        file.write(out)
    
    print('Keyboard run')