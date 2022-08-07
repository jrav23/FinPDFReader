#PDFReader
# This program aims to read pdf financial statements and convert them to csvs

from ast import Return
from distutils.command.build_scripts import first_line_re
from operator import delitem
from posixpath import split
from tkinter.messagebox import RETRY
import PyPDF2
import os
from pynput.keyboard import Key, Controller
import time
import Keyboard
import csv

class PDFReader:

    ## Utility Functions
    # def cleanCurrency(self,):
    # def checkNumber(self,):
    # def checkCurrency(self,):

    ## Convert PDFs to txt

    def convertPDFtoTxt(self, files):
        keyboard = Keyboard()
        keyboard.convertPDFtoTxt(files)

    ## Convert txt to csv
    def isEndPercent(self, line):
        if line[-1] == "%":
            return True
        return False

    def isEndNumber(self, line):
        if len(line) - line.find('.') == 3:
            return True
        return False
    
    def isNumber(self, line, index):
        if line[index] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return True
        return False

    def hasCurrency(self, line):
        deci = line.find('.')
        if self.isNumber(line, deci-1) and self.isNumber(line, deci+1):
            if self.isNumber(line, deci+2):
                return True
        return False
    
    def isPositive(self, line):
        isNeg = 0
        if line[isNeg] == "-":
            return False
        return True

    def isNotBreak(self, char):
        if not self.isNumber(char, 0):
            if char not in ['-', '$', '%', '.', ',']:
                return False
        return True

    def cleanCurrency(self, currency):
        c1 = currency.replace(',','')
        if not self.isPositive(currency):
            return '-$' + c1[1:]
        else:
            return '$' + c1

    def getLineitemsIS(self, line):
        i = line.find('.')
        j = i + line[i:].find(' ') + 1
        while self.isNotBreak(line[i]):
            i -= 1
        return line[:i] + ',' + self.cleanCurrency(line[i+1:j-1]) + ',' + line[j:]  

    def csv_writer(self, data, fileName):
        with open(fileName,'w') as outputFile:
            outputFile.write(data)
            outputFile.close()

        
    def getLineitemsBS(self, line):
        i = line.find('.')
        while self.isNotBreak(line[i]):
            i -= 1
        return line[:i] + ',' + self.cleanCurrency(line[i+1:])

    # IS
    def IScsv(self, files, filepath):
        for file in files:
            fp = filepath + file
            openFile = open(fp).read()
            lines = openFile.split('\n')
            csv = ""
            first = True
            pbCount = 0
            for line in lines:
                line = str(line)
                if first:
                    first = False
                    csv += 'first,' + line + '\n'
                elif self.isEndPercent(line):
                    if self.hasCurrency(line):
                        csv += 'lineitem,' + self.getLineitemsIS(line) + '\n'
                else:
                    if len(line) > 1:
                        if line[1] == ":":
                            pbCount = 5
                    if pbCount > 0:
                        pbCount -= 1
                    else:
                        csv += 'title,' + line + '\n'
            fpCSV = fp[:-4] + '.csv'
            self.csv_writer(csv,fpCSV)
            print('Saved ' + fpCSV)
            

    # BS
    def BScsv(self, files, filepath):
        for file in files:
            fp = filepath + file
            openFile = open(fp).read()
            lines = openFile.split('\n')
            csv = ""
            first = True
            pbCount = 0
            for line in lines:
                line = str(line)
                if first:
                    first = False
                    csv += 'first,' + line + '\n'
                elif self.hasCurrency(line):
                    csv += 'lineitem,' + self.getLineitemsBS(line) + '\n'
                else:
                    if line[1] == ":":
                        pbCount = 5
                    if pbCount > 0:
                        pbCount -= 1
                    else:
                        csv += 'title,' + line + '\n'
            fpCSV = fp[:-4] + '.csv'
            self.csv_writer(csv,fpCSV)
            print('Saved ' + fpCSV)


    ## read up txt/pdf file
    def readPDF(self, file):
        with open(file,'rb') as fileOpen:
            pdf = PyPDF2.PdfFileReader(fileOpen)
            text = ""
            for i in range(pdf.getNumPages()):
                page = pdf.getPage(i)
                text += str(page.extractText()).replace('\n','')
            print(text)
            fileOpen.close()
            
    def readTxt(self, file):
        fileOpen = open(file)
        pdf = fileOpen.read()
        print(type(fileOpen))

    ## figure out file type

    ## Sort into csv

    ## Save


    def __init__(self):
        print('Hello PDFReader')
