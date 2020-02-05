#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe Game

Created on Sat Feb  1 10:50:11 2020

@author: frbvianna
"""

posNumber = {"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}

choseReplay = True

def greet():
    """ Introduces the game and decides player X or O """
    
    print("\n\nTIC-TAC-TOE: \nWelcome to Tic-Tac-Toe!\n")
    
    global playerOne
    global playerTwo
    
    playerOne = ""
    playerTwo = ""
    
    while not (playerOne == 'X' or playerOne == 'O'):
        playerOne = input("Player 1: Would you like to be X or O? ")
    else:
            if playerOne == 'O':
                playerTwo = 'X'
            else:
                playerTwo = 'O'
                
    print(f"\nPlayer 1: ( {playerOne} )")
    print(f"Player 2: ( {playerTwo} )")
    print("\nPlayer 1 starts the game!")
    

def printBoard():
    """ Fetches "posNumber" dictionary board values as a list, addressing each position in the board print f-string """
    
    posList = list(posNumber.values())

    print(f" __________ __________ __________ \n|     {posList[6]}    |     {posList[7]}    |     {posList[8]}    |\n|__________|__________|__________|\n|     {posList[3]}    |     {posList[4]}    |     {posList[5]}    |\n|__________|__________|__________|\n|     {posList[0]}    |     {posList[1]}    |     {posList[2]}    |\n|__________|__________|__________|\n")    


def clearBoard():
    """ Generates 30 new empty lines for visual cleanse of console"""
    
    print("\n"*30)
    
    
def clearVars():
    """ Empties player entries, win variable and "posNumber" dictionary board values """
    
    global posNumber
    global playerOne
    global playerTwo
    global win

    playerOne = ''
    playerTwo = ''
    
    win = ''
    
    for i in list(posNumber.keys()):
        posNumber[i] = " "

    
def selectPos(turn):
    """ Selects input position on the board and links it to matching "posNumber" dictionary board value """
    
    if turn == playerOne:
        posInput = ""
        while not posInput in list(posNumber.keys()):
            posInput = input("P1: Input a corresponding 1-9 position in the Num Keyboard: ")
            while not posNumber[posInput] == " ":
                print("Position occupied.")
                posInput = input("P1: Input a corresponding 1-9 position in the Num Keyboard: ")
        
        posNumber[posInput] = playerOne
        
    if turn == playerTwo:
        posInput = ""
        while not posInput in list(posNumber.keys()):
            posInput = input("P2: Input a corresponding 1-9 position in the Num Keyboard: ")
            while not posNumber[posInput] == " ":
                print("Position occupied.")
                posInput = input("P2: Input a corresponding 1-9 position in the Num Keyboard: ")
                
        posNumber[posInput] = playerTwo
        
def decideMatch():
    """ For every possible win combination, tests whether X or O marks comply, returning the win variable whenever someone wins """
    
    combinations = (['1','2','3'],['2','5','8'],['4','5','6'],['7','8','9'],['1','4','7'],['9','6','3'],['7','5','3'],['1','5','9'])
    winMatch = ''
    
    for trio in combinations:
        testPlayerOne = [playerOne]*3
        testPlayerTwo = [playerTwo]*3
        
        for pos in trio:  
            if posNumber[pos] == playerOne:
                testPlayerOne.pop()
                if testPlayerOne == []:
                    winMatch = "1"
                    break
                    
            if posNumber[pos] == playerTwo:
                testPlayerTwo.pop()
                if testPlayerTwo == []:
                    winMatch = "2"
                    break
    
    return winMatch

def tttRun(keepRun, whoseTurn):
    """ While no one has won the game, keeps alternating player turns and printing their marks on the board """
    
    while keepRun == '':
        clearBoard()
        printBoard()
            
        if whoseTurn == playerOne:
            whoseTurn = playerTwo
            selectPos(whoseTurn)
        else:
            whoseTurn = playerOne
            selectPos(whoseTurn)

        keepRun = decideMatch()
    
    return keepRun

def end(whoWon):
    """ States who's the winner, clears variables and returns replay decision """
    
    print("Player {} won!".format(whoWon))
    clearVars()
    endInput = input("Would you like to play again? [Yes (y) or No (n)]: ")
    return replay(endInput)       
        
def replay(choice):
    """ Returns True for a replay or False for no replay """
    
    return (choice == 'Yes' or choice == 'Y' or choice == 'y' or choice == 'yes')

       
def ticTacToe():
    """ Tic-Tac-Toe Console Minigame\n
        Function to call for game run\n
        Optimized for Spyder IDE console
    """
    
    clearVars()
    
    global playerOne
    global playerTwo
    global choseReplay
    
    playerOne = ""
    playerTwo = ""    
    
    while choseReplay:
        
        greet()
        
        whoseTurn = playerOne
        selectPos(whoseTurn)
        
        win = decideMatch()
        
        untilEnd = tttRun(win, whoseTurn)
        
        clearBoard()
        printBoard()
        choseReplay = end(untilEnd)
        
    else:
        print("Thanks for playing!")
            
        
                
        
              
