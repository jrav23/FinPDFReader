
import PDFReader

if __name__ == "__main__":
    
    filePath = "C:/Users/joeyr/OneDrive/Documents/ACT/02_Prospects/OMG/Sandland43, LLC/"
    running = True
    savesGOMG = ['GOMG 21 IS.txt', 'GOMG 21 BS.txt', 'GOMG 20 IS.txt', 'GOMG 20 BS.txt', 'GOMG 19 IS.txt', 'GOMG 19 BS.txt', 'GOMG 18 IS.txt', 'GOMG 18 BS.txt', 'GOMG 17 IS.txt', 'GOMG 17 BS.txt']
    savesGUKT = ['GUKT 21 IS.txt', 'GUKT 21 BS.txt', 'GUKT 20 IS.txt', 'GUKT 20 BS.txt', 'GUKT 19 IS.txt', 'GUKT 19 BS.txt', 'GUKT 18 IS.txt', 'GUKT 18 BS.txt', 'GUKT 17 IS.txt', 'GUKT 17 BS.txt']
    savesMission = ['Mission 21 IS.txt', 'Mission 21 BS.txt']
    savesRGroup = ['RGroup 21 IS.txt', 'RGroup 21 BS.txt', 'RGroup 20 IS.txt', 'RGroup 20 BS.txt', 'RGroup 19 IS.txt', 'RGroup 19 BS.txt', 'RGroup 18 IS.txt', 'RGroup 18 BS.txt', 'RGroup 17 IS.txt', 'RGroup 17 BS.txt']
    savesPBAH = ['PBAH 21 IS.txt', 'PBAH 21 BS.txt', 'PBAH 20 IS.txt', 'PBAH 20 BS.txt', 'PBAH 19 IS.txt', 'PBAH 19 BS.txt', 'PBAH 18 IS.txt', 'PBAH 18 BS.txt', 'PBAH 17 IS.txt', 'PBAH 17 BS.txt']
    savesSandland = ['Sandland 21 IS.txt', 'Sandland 21 BS.txt', 'Sandland 20 IS.txt', 'Sandland 20 BS.txt', 'Sandland 19 IS.txt', 'Sandland 19 BS.txt', 'Sandland 18 IS.txt', 'Sandland 18 BS.txt', 'Sandland 17 IS.txt', 'Sandland 17 BS.txt']

    saveTest = ['GOMG 21 IS.txt', 'GOMG 21 BS.txt']

    while running:
        task = input('Enter Task:\n["e" - Exit Program, "r" - Run Schedule]\n')
        if task == 'e':
            running = False
        elif task == 'r':
            reader = PDFReader.PDFReader()
            task = input('Enter Task:\n["c" - ISBScsv]\n')
            if task == 'c':
                for save in savesSandland:
                    deci = save.find('.')
                    fileType = save[deci-2:deci]
                    if fileType == 'IS':
                        reader.IScsv([save],filePath)
                    elif fileType == 'BS':
                        reader.BScsv([save],filePath)

        print('end running')
    print('Ran Main')
