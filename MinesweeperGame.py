#Kevin Babakhani - MinesweeperGame.py
#CS/IS 151 - Summer 2022 Course
#08/16/2022

import Minesweeper


def main():
    
    selection = ""
    
    gType = ""
    
    minesweeperGame = Minesweeper.MinesweeperClass()
    
    minesweeperGame.minesweeperIntro()

    while(selection != 'q' and selection != 'Q'):
    
        print("""MINE SWEEPER GAME 
------------------ 
i) Display Game Instructions 
p) Play Game 
s) Print Statistics and Save to a File 
q) Quit""")
    
        selection = input("Please make a selection: ")
    
    
        if(selection == 'i' or selection == 'I'):
        
            print("""\nMINE SWEEPER GAME RULES
-----------------------
OBJECTIVE: Your objective is to rule 
out the entire grid without hitting a bomb.
Once all of the grid is ruled out and no bombs are hit,
you win! BUT...if you even hit one bomb, YOU LOSE!
HAVE FUN! :)\n""")        
        
  
        elif(selection == 'p' or selection == 'P'):
            

            gType = input("\nWould you like to play at the Beginner level or the Intermediate level? (enter b/B or i/I) ")
            minesweeperGame.setGameType(gType)
        
        
            while(minesweeperGame.getGameType() != 'b' and minesweeperGame.getGameType() != 'B' and minesweeperGame.getGameType() != 'i' and minesweeperGame.getGameType() != 'I'):
                
                print("Invalid Selection!")
                gType = input("\nWould you like to play at the Beginner level or the Intermediate level? (enter b/B or i/I) ")
                minesweeperGame.setGameType(gType)
                
        
            if(minesweeperGame.getGameType() == 'b' or minesweeperGame.getGameType() == 'B'):
             
                print()   
                minesweeperGame.setBeginnerGamesPlayed(minesweeperGame.getBeginnerGamesPlayed() + 1)
                minesweeperGame.setGamesPlayed(minesweeperGame.getGamesPlayed() + 1)
                minesweeperGame.setRow(10)
                minesweeperGame.setCol(10)    
                minesweeperGame.createBoard()
                minesweeperGame.displayBoard(minesweeperGame.getRow())  
                minesweeperGame.scatterBombs()    
                
                minesweeperGame.getUserRowAndCol()    
                minesweeperGame.makeMove(minesweeperGame.getUserRow(), minesweeperGame.getUserCol())   
                

                while(minesweeperGame.checkWin(minesweeperGame.getUserRow(), minesweeperGame.getUserCol()) == 2):
                                                      
                    minesweeperGame.getUserRowAndCol() 
                    minesweeperGame.makeMove(minesweeperGame.getUserRow(), minesweeperGame.getUserCol())   
                                 
            
            
            elif(minesweeperGame.getGameType() == 'i' or minesweeperGame.getGameType() == 'I'):
                
                print()
                minesweeperGame.setIntermediateGamesPlayed(minesweeperGame.getIntermediateGamesPlayed() + 1)
                minesweeperGame.setGamesPlayed(minesweeperGame.getGamesPlayed() + 1)
                minesweeperGame.setRow(15)
                minesweeperGame.setCol(15)
                minesweeperGame.createBoard()
                minesweeperGame.displayBoard(minesweeperGame.getRow())
                minesweeperGame.scatterBombs()
                
                minesweeperGame.getUserRowAndCol()    
                minesweeperGame.makeMove(minesweeperGame.getUserRow(), minesweeperGame.getUserCol())   
                

                while(minesweeperGame.checkWin(minesweeperGame.getUserRow(), minesweeperGame.getUserCol()) == 2):
                                                      
                    minesweeperGame.getUserRowAndCol() 
                    minesweeperGame.makeMove(minesweeperGame.getUserRow(), minesweeperGame.getUserCol())             
                
                
        elif(selection == 's' or selection == 'S'):
                
            try:
                minesweeperGame.writeStats()
                minesweeperGame.readStats()
                
            except:
                print("""\nCannot print stats, error\n""")

        elif(selection == 'q' or selection == 'Q'):
    
            input("\nThank you for using the program!") 
            
        
        else:
            
            print("\nInvalid Selection!\n")
            
      
if __name__ == '__main__':
    main()