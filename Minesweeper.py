#Kevin Babakhani - Minesweeper.py
#CS/IS 151 - Summer 2022 Course
#08/16/2022

import random

import matplotlib.pyplot as plt

from tkinter import *
import tkinter.messagebox

class MinesweeperClass:
    
    def __init__(self):
        self.beginnerGamesPlayed = 0
        self.setBeginnerGamesPlayed(0)
        
                
        self.intermediateGamesPlayed = 0
        self.setIntermediateGamesPlayed(0)
        
    
        self.beginnerGamesWon = 0
        self.setBeginnerGamesWon(0)
                
                
        self.intermediateGamesWon = 0   
        self.setIntermediateGamesWon(0)
        
        
        
        self.row = 0
        self.col = 0
        
        self.setRow(0)
        self.setCol(0)
        
        self.userRow = ""
        self.userCol = ""
        
        self.setUserRow("")
        self.setUserCol("")        
        
    
        self.gamesPlayed = 0
        self.gamesWon = 0  
        
        self.setGamesPlayed(0)
        self.setGamesWon(0)          
        
        self.gameType = ""
        self.setGameType("")
        
        
    
    def createBoard(self):
        
        self.mineField = [[0] * self.getCol() for _ in range(self.getRow())]
        
        for r in range(self.getRow()):
            for c in range(self.getCol()):
                self.mineField[r][c] = "x"
                         
                
    def scatterBombs(self):
        
        num = 0
        
        self.bombs = [[0] * self.getCol() for _ in range(self.getRow())]
        
        for r in range(self.getRow()):
            for c in range(self.getCol()):
                num = (random.randrange(2) + 1)
                if(num == 1):
                    self.bombs[r][c] = "*"
                    
                elif(num == 2):
                    self.bombs[r][c] = "x"   
           
         
        for r in range(self.getRow()):
            for c in range(self.getCol()):
                if(self.bombs[r][c] != "*" and self.getAdjMineCount(r, c) != 0):
                    self.bombs[r][c] = self.getAdjMineCount(r, c)    
                    
                elif(self.bombs[r][c] != "*" and self.getAdjMineCount(r, c) == 0):
                    self.bombs[r][c] = "."     

    
    def displayBoard(self, row):
        
        if(row == 10):
            
            print("""MINESWEEPER GAME BOARD 
---------------------- 
 
   0 1 2 3 4 5 6 7 8 9  
   -------------------- """)
            
            for r in range(self.getRow()):
                print(str(r) + "|" , end = ' ')
                for c in range(self.getCol()):
                    print(self.mineField[r][c], end = ' ')
                print()            
            
        else:
            print("""MINESWEEPER GAME BOARD 
---------------------- 
 
    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14  
   -------------------------------------------- """)            
            for r in range(self.getRow()):
                if(r<10):
                    print(str(r) + " |" , end = ' ')
                else:
                    print(str(r) + "|" , end = ' ')               
                for c in range(self.getCol()):
                    print(self.mineField[r][c], end = '  ')
                print()        
        print()

    
    def genAnswerBoard(self):

        if(self.getRow() == 10):
            
            print(""" 
   0 1 2 3 4 5 6 7 8 9  
   -------------------- """)
            
            for r in range(self.getRow()):
                print(str(r) + "|" , end = ' ')
                for c in range(self.getCol()):
                    if(self.bombs[r][c] == "*"):
                        print("@", end = ' ')
                    else:
                        print(self.bombs[r][c], end = ' ')
                print()            
            
        else:
            
            print(""" 
    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14  
   -------------------------------------------- """)            
            for r in range(self.getRow()):
                if(r<10):
                    print(str(r) + " |" , end = ' ')
                else:
                    print(str(r) + "|" , end = ' ')               
                for c in range(self.getCol()):
                    if(self.bombs[r][c] == "*"):
                        print("@ ", end = ' ')
                    else:
                        print(self.bombs[r][c], " ", end = '')
                print()        
        print()      
            
    def genAnswerBoardTwo(self):
        
        if(self.getRow() == 10):
            
            print(""" 
   0 1 2 3 4 5 6 7 8 9  
   -------------------- """)
            
            for r in range(self.getRow()):
                print(str(r) + "|" , end = ' ')
                for c in range(self.getCol()):
                    print(self.bombs[r][c], end = ' ')
                print()            
            
        else:
            
            print(""" 
    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14  
   -------------------------------------------- """)            
            for r in range(self.getRow()):
                if(r<10):
                    print(str(r) + " |" , end = ' ')
                else:
                    print(str(r) + "|" , end = ' ')               
                for c in range(self.getCol()):
                    print(self.bombs[r][c], end = '  ')
                print()        
        print()     
    
    
    def getAdjMineCount(self, row, col):
        
        count = 0
        
        if(row != 0 and col != 0):
            if(self.bombs[row-1][col-1] == "*"):
                count = (count + 1)

        if(row != 0):
            if(self.bombs[row-1][col] == "*" and row != 0):
                count = (count + 1)
            
        if((self.getGameType() == 'b' or self.getGameType() == 'B') and row != 0 and col != 9):
            if(self.bombs[row-1][col+1] == "*"):
                count = (count + 1)
                
        elif((self.getGameType() == 'i' or self.getGameType() == 'I') and row != 0 and col != 14):
            if(self.bombs[row-1][col+1] == "*"):
                count = (count + 1)            
            
        if((self.getGameType() == 'b' or self.getGameType() == 'B') and col != 9):
            if(self.bombs[row][col+1] == "*"):
                count = (count + 1)
                
        elif((self.getGameType() == 'i' or self.getGameType() == 'I') and col != 14):
            if(self.bombs[row][col+1] == "*"):
                count = (count + 1)   
            
        if((self.getGameType() == 'b' or self.getGameType() == 'B') and col != 9 and row != 9):
            if(self.bombs[row+1][col+1] == "*"):
                count = (count + 1)
                
        elif((self.getGameType() == 'i' or self.getGameType() == 'I') and col != 14 and row != 14):
            if(self.bombs[row+1][col+1] == "*"):
                count = (count + 1) 
            
        if((self.getGameType() == 'b' or self.getGameType() == 'B') and row != 9):
            if(self.bombs[row+1][col] == "*"):
                count = (count + 1)
                
        elif((self.getGameType() == 'i' or self.getGameType() == 'I') and row != 14):
            if(self.bombs[row+1][col] == "*"):
                count = (count + 1) 
            
        if((self.getGameType() == 'b' or self.getGameType() == 'B')  and row != 9 and col != 0):
            if(self.bombs[row+1][col-1] == "*"):
                count = (count + 1)
                
        elif((self.getGameType() == 'i' or self.getGameType() == 'I')  and row != 14 and col != 0):
            if(self.bombs[row+1][col-1] == "*"):
                count = (count + 1) 
            
        if(col != 0):
            if(self.bombs[row][col-1] == "*"):
                count = (count + 1)     
            
        return count

    
    def checkWin(self, row, col):
        
        answer = 0
        
        if(self.bombs[int(row)][int(col)] == "*"):
            answer = 1
            print("""\nSORRY YOU LOST! :-(  
PLEASE PLAY AGAIN – BETTER LUCK NEXT TIME. \n""")   
            print("\nFinal Board: \n")
            self.genAnswerBoardTwo()
            print()
            
        
        else: 
            for r in range(self.getRow()):
                for c in range(self.getCol()):
                    if(self.bombs[r][c] != "*" and self.mineField[r][c] == "x"):
                        answer = 2

            
            if(answer == 2):
                print("\nGame not won yet, continue...\n")   
                        
            elif(answer == 0):
                
                if(self.getGameType() == 'b' or self.getGameType() == 'B'):
                    self.setBeginnerGamesWon(self.getBeginnerGamesWon() + 1)
                    
                elif(self.getGameType() == 'i' or self.getGameType() == 'I'):   
                    self.setIntermediateGamesWon(self.getIntermediateGamesWon() + 1)
                    
                print("\nCONGRATULATIONS! YOU WIN!!! :-)\n")  
                print("\nFinal Board: \n")
                self.genAnswerBoard()
                print()
            
        return answer

    
    def makeMove(self, row, col):
        
        if(self.bombs[row][col] == "."):
            if(row != 0 and col != 0):
                self.mineField[row-1][col-1] = self.bombs[row-1][col-1]
    
            if(row != 0):
                self.mineField[row-1][col] = self.bombs[row-1][col]
                
            if((self.getGameType() == 'b' or self.getGameType() == 'B') and row != 0 and col != 9):
                self.mineField[row-1][col+1] = self.bombs[row-1][col+1]
                    
            elif((self.getGameType() == 'i' or self.getGameType() == 'I') and row != 0 and col != 14):
                self.mineField[row-1][col+1] = self.bombs[row-1][col+1]     
                
            if((self.getGameType() == 'b' or self.getGameType() == 'B') and col != 9):
                self.mineField[row][col+1] = self.bombs[row][col+1]
                    
            elif((self.getGameType() == 'i' or self.getGameType() == 'I') and col != 14):
                self.mineField[row][col+1] = self.bombs[row][col+1]
                
            if((self.getGameType() == 'b' or self.getGameType() == 'B') and col != 9 and row != 9):
                self.mineField[row+1][col+1] = self.bombs[row+1][col+1]
                    
            elif((self.getGameType() == 'i' or self.getGameType() == 'I') and col != 14 and row != 14):
                self.mineField[row+1][col+1] = self.bombs[row+1][col+1]
                
            if((self.getGameType() == 'b' or self.getGameType() == 'B') and row != 9):
                self.mineField[row+1][col] = self.bombs[row+1][col]
                    
            elif((self.getGameType() == 'i' or self.getGameType() == 'I') and row != 14):
                self.mineField[row+1][col] = self.bombs[row+1][col]
                
            if((self.getGameType() == 'b' or self.getGameType() == 'B')  and row != 9 and col != 0):
                self.mineField[row+1][col-1] = self.bombs[row+1][col-1]
                    
            elif((self.getGameType() == 'i' or self.getGameType() == 'I')  and row != 14 and col != 0):
                self.mineField[row+1][col-1] = self.bombs[row+1][col-1]
                
            if(col != 0):
                self.mineField[row][col-1] = self.bombs[row][col-1] 
            
        self.mineField[row][col] = self.bombs[row][col]   
                              
        print("\nUpdated Board: \n")
                
        if(self.getRow() == 10):
            
            print(""" 
   0 1 2 3 4 5 6 7 8 9  
   -------------------- """)     
            
            for r in range(self.getRow()):
                print(str(r) + "|" , end = ' ')
                for c in range(self.getCol()):
                    print(self.mineField[r][c], end = ' ')
                print()      
                
        else:
            
            print(""" 
    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14  
   -------------------------------------------- """)     
                
            for r in range(self.getRow()):
                if(r<10):
                    print(str(r) + " |" , end = ' ')
                else:
                    print(str(r) + "|" , end = ' ')               
                for c in range(self.getCol()):
                    print(self.mineField[r][c], end = '  ')
                print()        
        print()       
            
    
    def getBeginnerGamesPlayed(self):

        return self.beginnerGamesPlayed

    
    def setBeginnerGamesPlayed(self, begGamesPlayed):
 
        self.beginnerGamesPlayed = begGamesPlayed
    
    
    
    def getIntermediateGamesPlayed(self):

        return self.intermediateGamesPlayed

    
    def setIntermediateGamesPlayed(self, intGamesPlayed):
 
        self.intermediateGamesPlayed = intGamesPlayed      
        
        
        
    def getBeginnerGamesWon(self):

        return self.beginnerGamesWon

    
    def setBeginnerGamesWon(self, begGamesWon):
 
        self.beginnerGamesWon = begGamesWon
    
    
    
    def getIntermediateGamesWon(self):

        return self.intermediateGamesWon

    
    def setIntermediateGamesWon(self, intGamesWon):
 
        self.intermediateGamesWon = intGamesWon   
        
        
        
    def getGamesWon(self):

        return self.gamesWon
    
    def setGamesWon(self, gWon):

        self.gamesWon = gWon  
        
    
    
    def getGamesPlayed(self):

        return self.gamesPlayed    
    
    def setGamesPlayed(self, gPlayed):

        self.gamesPlayed = gPlayed    
        
    
    
    def getGameType(self):

        return self.gameType
    
    def setGameType(self, gType):

        self.gameType = gType        
        
        
        
    def getRow(self):

        return self.row
    
    def setRow(self, theRow):

        self.row = theRow      
        
    def getCol(self):

        return self.col
    
    def setCol(self, theCol):

        self.col = theCol     
         
        
    def getUserRow(self):

        return self.userRow
    
    def setUserRow(self, theRow):

        self.userRow = theRow      
        
    def getUserCol(self):

        return self.userCol
    
    def setUserCol(self, theCol):

        self.userCol = theCol           
        
        
    def getMineFieldData(self, row, col):
        
        return self.mineField[row][col]
    
    def getUserRowAndCol(self):
        
        if(self.getGameType() == "b" or self.getGameType() == "B"):
                        
            self.userRow = input("Enter a row for the board (0-9): ")
        
        
            if(self.userRow.lstrip("-").isdigit() == True or self.userRow.lstrip("-").isdigit() == False):
                while(self.userRow.isdigit() == False or int(self.userRow) < 0 or int(self.userRow) > 9):
                    print("Invalid Row, Try Again.")
                    self.userRow = input("Enter a row for the board (0-9): ")                       
         
        
            self.userCol = input("Enter a column for the board (0-9): ")
          
            if(self.userCol.lstrip("-").isdigit() == True or self.userCol.lstrip("-").isdigit() == False):
                while(self.userCol.isdigit() == False or int(self.userCol) < 0 or int(self.userCol) > 9):
                    print("Invalid Column, Try Again.")
                    self.userCol = input("Enter a column for the board (0-9): ")                           
            
        
            while(self.mineField[int(self.userRow)][int(self.userCol)] != "x"):
                print("Spot already chosen, try again")
                self.userRow = input("Enter a row for the board (0-9): ")
                self.userCol = input("Enter a column for the board (0-9): ")
            
            
                if(self.userRow.lstrip("-").isdigit() == True or self.userRow.lstrip("-").isdigit() == False):
                    while(self.userRow.isdigit() == False or int(self.userRow) < 0 or int(self.userRow) > 9):
                        print("Invalid Row, Try Again.")
                        self.userRow = input("Enter a row for the board (0-9): ")                       
                
                
                if(self.userCol.lstrip("-").isdigit() == True or self.userCol.lstrip("-").isdigit() == False):
                    while(self.userCol.isdigit() == False or int(self.userCol) < 0 or int(self.userCol) > 9):
                        print("Invalid Column, Try Again.")
                        self.userCol = input("Enter a column for the board (0-9): ")  
                        
                         
            self.userRow = int(self.userRow)
            self.userCol = int(self.userCol)     

                
        elif(self.getGameType() == "i" or self.getGameType() == "I"):
                        
            self.userRow = input("Enter a row for the board (0-14): ")
        
        
            if(self.userRow.lstrip("-").isdigit() == True or self.userRow.lstrip("-").isdigit() == False):
                while(self.userRow.isdigit() == False or int(self.userRow) < 0 or int(self.userRow) > 14):
                    print("Invalid Row, Try Again.")
                    self.userRow = input("Enter a row for the board (0-14): ")                       
         
        
            self.userCol = input("Enter a column for the board (0-14): ")
          
            if(self.userCol.lstrip("-").isdigit() == True or self.userCol.lstrip("-").isdigit() == False):
                while(self.userCol.isdigit() == False or int(self.userCol) < 0 or int(self.userCol) > 14):
                    print("Invalid Column, Try Again.")
                    self.userCol = input("Enter a column for the board (0-14): ")                           
            
        
            while(self.mineField[int(self.userRow)][int(self.userCol)] != "x"):
                print("Spot already chosen, try again")
                self.userRow = input("Enter a row for the board (0-14): ")
                self.userCol = input("Enter a column for the board (0-14): ")
            
            
                if(self.userRow.lstrip("-").isdigit() == True or self.userRow.lstrip("-").isdigit() == False):
                    while(self.userRow.isdigit() == False or int(self.userRow) < 0 or int(self.userRow) > 14):
                        print("Invalid Row, Try Again.")
                        self.userRow = input("Enter a row for the board (0-14): ")                       
                
                
                if(self.userCol.lstrip("-").isdigit() == True or self.userCol.lstrip("-").isdigit() == False):
                    while(self.userCol.isdigit() == False or int(self.userCol) < 0 or int(self.userCol) > 14):
                        print("Invalid Column, Try Again.")
                        self.userCol = input("Enter a column for the board (0-14): ")  
                         
            self.userRow = int(self.userRow)
            self.userCol = int(self.userCol)     
            
    def minesweeperIntro(self):
        
        self.mainWindow = Tk()
        
        self.mainWindow.title("Minesweeper Intro")
        
        self.topFrame = Frame(self.mainWindow)
        self.bottomFrame = Frame(self.mainWindow)
        
        self.mainWindow.configure(bg = "red")      
        
        self.label1 = Label(self.mainWindow, 
        text = """Welcome to Minesweeper!\n 
Before we begin,\n
select a confidence level (1 to 5) to get a message from the creator depending on how confident you\n 
are in your ability to win. After viewing the message, select the 'Quit' button to resume your game, good luck!!!""", bg = "green", fg = "black")
        
        
        self.label1.pack(side = "top", fill = 'x')
        
        
        self.radioVar = IntVar()
        
        self.radioVar.set(1)
        
        self.rb1 =  Radiobutton(self.topFrame,
                    text = "Confidence Level 1", variable = self.radioVar,
                    value = 1, bg = "orange")
        
        self.rb2 = Radiobutton(self.topFrame,
                    text = "Confidence Level 2", variable = self.radioVar,
                    value = 2, bg = "orange")
        
        self.rb3 = Radiobutton(self.topFrame,
                    text = "Confidence Level 3", variable = self.radioVar,
                    value = 3, bg = "orange")
        
        self.rb4 =  Radiobutton(self.topFrame,
                    text = "Confidence Level 4", variable = self.radioVar,
                    value = 4, bg = "orange")
        
        self.rb5 = Radiobutton(self.topFrame,
                    text = "Confidence Level 5", variable = self.radioVar,
                    value = 5, bg = "orange")    
        
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        self.rb5.pack()      
        
        self.okButton = Button(self.bottomFrame,
                      text = "OK", command = self.showChoice, bg = "light blue", fg = "green", font = ("Times", 12, "bold"))
        
        self.quitButton = Button(self.bottomFrame,
                      text = "Quit", command = self.mainWindow.quit, bg = "pink", fg = "red", font = ("Times", 12, "bold"))

        self.okButton.pack(side = "left")
        self.quitButton.pack(side = "left")

        self.topFrame.pack()
        self.bottomFrame.pack()
        
        self.mainWindow.mainloop()      
        
    def showChoice(self):
        
        if(str(self.radioVar.get()) == "1"):
            tkinter.messagebox.showinfo("Selection", "HEY...that is ok, DO NOT give up!")
        elif(str(self.radioVar.get()) == "2"):
            tkinter.messagebox.showinfo("Selection", "Could be better, but you still have a fighting chance!")
        elif(str(self.radioVar.get()) == "3"):
            tkinter.messagebox.showinfo("Selection", "This game could go either way, try your best!")
        elif(str(self.radioVar.get()) == "4"):
            tkinter.messagebox.showinfo("Selection", "Great, I am sure you will win!")
        elif(str(self.radioVar.get()) == "5"):
            tkinter.messagebox.showinfo("Selection", "I am expecting a BIG win here!")
       
     
    def readStats(self):
        
        try:
            
            infile = open('stats.txt', 'r')
            
            for string in infile:
        
                sentence = str(string)
        
                print(sentence)            
             
            
            infile.close()
            
            
        except:
        
            print('An error occurred.')                
        
        
        
    def writeStats(self):
        
        if(self.beginnerGamesPlayed == 0):
            numOne = 0.0
            
        else:
            numOne = (self.beginnerGamesWon / self.beginnerGamesPlayed * 100)
            
            
        if(self.intermediateGamesPlayed == 0):
            numTwo = 0.0       
            
        else:
            numTwo = (self.intermediateGamesWon / self.intermediateGamesPlayed * 100)
            
            
        if(self.gamesPlayed == 0):
            numThree = 0.0
            
        else:
            numThree = ((self.beginnerGamesWon + self.intermediateGamesWon) / (self.gamesPlayed) * 100)           


        if(numOne == 0.0 and numTwo == 0.0 and numThree == 0.0):
            pieOne = [1, 1, 0]
        else:
            pieOne = [numOne, numTwo, numThree]

            
        if(self.beginnerGamesWon == 0 and self.intermediateGamesWon == 0 and self.gamesWon == 0):
            pieTwo = [1, 1, 0]
        else:
            pieTwo = [self.beginnerGamesWon, self.intermediateGamesWon, self.gamesWon]
                  
        pieOneLabels = ["Beginner Win Percentage", "Intermediate Win Percentage", "Overall Win Percentage"]
        
        pieTwoLabels = ["Beginner Games Won", "Intermediate Games Won", "Total Games Won"]
        
        try:
            
                
            outfile = open('stats.txt', 'w')
                    
            outfile.write("""\nMINESWEEPER STATISTICS REPORT 
----------------------------- 
BEGINNER GAMES:         INTERMEDIATE GAMES: \n""")
                    
            outfile.write("   Games Played: " + str(self.beginnerGamesPlayed) + "\t" + "   Games Played: " + str(self.intermediateGamesPlayed) + "\n")
                
            outfile.write("   Games Won: " + str(self.beginnerGamesWon) + "\t\t" + "   Games Won: " + str(self.intermediateGamesWon) + "\n")
                
            outfile.write("\nPercentage Wins:" + "\n")
                
            outfile.write("\tBeginner:\t" + (f"{numOne:,.2f}") + "%" + "\n")
                
            outfile.write("\tIntermediate:\t" + (f"{numTwo:,.2f}") + "%" + "\n")
                
            outfile.write("\tOVERALL:\t" + (f"{numThree:,.2f}") + "%" + "\n")  
            
            outfile.close()
            
            
            plt.figure(0)
            
            plt.pie(pieOne, labels = pieOneLabels)
        
            plt.title('Minesweeper Win Percentages')
        
            plt.show()
            
            
            plt.figure(1)
            
            plt.pie(pieTwo, labels = pieTwoLabels)
        
            plt.title('Minesweeper Games Won')
        
            plt.show()            
            
            
        except:
        
            print("An error occurred.")