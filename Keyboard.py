# Keyboard controller for pdf reader

from re import S
from pynput.keyboard import Key, Controller
import time

# Mouse Imports


class Keyboard:
    keyboard = Controller()
        
    # basic windows functions
    def altTab(self):
        self.keyboard.press(Key.alt)
        self.keyboard.tap(Key.tab)
        self.keyboard.release(Key.alt)
        time.sleep(1)

    def ctrlAll(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.tap('a')
        self.keyboard.release(Key.ctrl)
        time.sleep(1)        

    def copy(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.tap('c')
        self.keyboard.release(Key.ctrl)
        time.sleep(1) 

    def paste(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.tap('v')
        self.keyboard.release(Key.ctrl)
        time.sleep(1)

    def cut(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.tap('x')
        self.keyboard.release(Key.ctrl)
        time.sleep(1)

    def openNotepad(self):
        self.keyboard.tap(Key.cmd)
        time.sleep(1)
        self.keyboard.type('notepad')
        time.sleep(1)
        self.keyboard.tap(Key.enter)
        time.sleep(1)

    def saveNotepad(self, fileName):
        self.keyboard.press(Key.ctrl)
        self.keyboard.tap('s')
        self.keyboard.release(Key.ctrl)
        time.sleep(1)
        self.keyboard.type(fileName)
        time.sleep(1)
        self.keyboard.tap(Key.enter)
        time.sleep(1)

    def closeWindow(self):
        self.keyboard.press(Key.alt)
        self.keyboard.tap(Key.f4)
        self.keyboard.release(Key.alt)
        time.sleep(1)

    def ctrlTab(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.tap(Key.tab)
        self.keyboard.release(Key.ctrl)
        time.sleep(1)

    def ctrlLetter(self, char):
        self.keyboard.press(Key.ctrl)
        self.keyboard.tap(char)
        self.keyboard.release(Key.ctrl)
        time.sleep(1)

    # Complex Functions
    def convertPDFtoTxt(self, saves):
        #start in VS Code
        #alt tab to PDF
        self.altTab()
        for tab in saves:
            self.ctrlAll()
            self.copy()
            self.openNotepad()
            self.paste()
            self.saveNotepad(tab)
            self.closeWindow()
            self.ctrlTab()

    def excelGoToA1(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.tap(Key.home)
        self.keyboard.release(Key.ctrl)
        time.sleep(1)

    def rightJustifyCells(self, rows, columnsRight, startC, startR, totalWidth): #need function to be able to input chars for startC
        # Ititially only the first column -
        # Start Excel cursur at the furthest right item in the first row and 
        # copy/paste to c columnsRight from there. Column in numbers
        
        self.altTab()
        self.excelGoToA1()
        for c in range(startC-1):
            self.keyboard.tap(Key.right)
            time.sleep(0.05)
        for r in range(startR-1):
            self.keyboard.tap(Key.down)
            time.sleep(0.05)
        self.cut()
        for cr in range(columnsRight):
            self.keyboard.tap(Key.right)
            time.sleep(0.05)
        self.paste()
        self.keyboard.tap(Key.down)
        self.keyboard.press(Key.ctrl)
        self.keyboard.tap(Key.left)
        self.keyboard.release(Key.ctrl)
        for n in range(rows-1):
            self.cut()
            time.sleep(0.5)
            self.keyboard.tap(Key.up)
            self.keyboard.press(Key.ctrl)
            for w in range(totalWidth):
                self.keyboard.tap(Key.right)
            self.keyboard.tap(Key.left)
            self.keyboard.release(Key.ctrl)
            self.keyboard.tap(Key.down)
            time.sleep(0.5)
            self.paste()
            time.sleep(0.5)
            self.keyboard.tap(Key.down)
            self.keyboard.press(Key.ctrl)
            self.keyboard.tap(Key.left)
            self.keyboard.release(Key.ctrl)
            time.sleep(0.5)
        time.sleep(1)
        print("complete right justify")

    def pullExcelColumnToCommaSepStringList(self, elements):
        time.sleep(10)
        while elements > 0:
            self.keyboard.press(Key.shift)
            self.keyboard.tap(Key.end)
            self.keyboard.release(Key.shift)
            self.keyboard.tap('\'')
            self.keyboard.tap(Key.right)
            self.keyboard.tap(Key.right)
            self.keyboard.tap(',')
            self.keyboard.tap(Key.space)
            self.keyboard.tap(Key.delete)
            time.sleep(1)
            elements -= 1

    def grabESPNNFL(self, gameIdStart = "401326638", numGames = 1):
        urlBase = "https://www.espn.com/nfl/boxscore/_/gameId/"
        url = urlBase + gameIdStart
        gameId = int(gameIdStart)
        time.sleep(4)

        if not isinstance(numGames,int):
            numGames = 0
            print('numGames needs to be an integer')
        
        if numGames < 0:
            numGames = 0
            print('numGames needs to be positive')
        
        if numGames >= 1:
            self.altTab()
            time.sleep(2)
            self.ctrlAll()
            self.copy()
            self.openNotepad()
            self.paste()
            self.saveNotepad("game" + str(gameId))
            self.closeWindow()
            gameId -= 1
            numGames -= 1

        while numGames > 0:
            self.ctrlLetter('t')
            self.keyboard.press(Key.shift)
            self.ctrlTab()
            self.keyboard.release(Key.shift)
            time.sleep(0.5)
            self.ctrlLetter('w')
            self.keyboard.type(urlBase + str(gameId))
            time.sleep(0.5)
            self.keyboard.tap(Key.enter)
            time.sleep(6)
            self.ctrlAll()
            self.copy()
            self.openNotepad()
            self.paste()
            self.saveNotepad("game" + str(gameId))
            self.closeWindow()
            gameId -= 1
            numGames -= 1

        self.ctrlTab()
        print('completed games ' + gameIdStart + ' to  ' + str(gameId))



    def __init__(self):
        self.keyboard = Controller()
        print('Hello Keyboard')