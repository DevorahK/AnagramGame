import random
import threading

highScores = [['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0]] #High scores are originally set to zero.
done = False
upperAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Random letters will be picked from here for the game grid.

def allDone(): #This function is what happens after the timer ends.
    print("Time's Up!")
    print("Press enter to continue") #Once the timer finished, the game's loop wouldn't end because it was stuck waiting for input. This is my inelegant solution.
    global done 
    done = True  #Now that this global variable 'done' = True, the game loop's condition will be met, and the loop will end.
    
def checkFile(word, file): #This function checks to see if a word is in the dictionary file.
    inFile = open(file, 'r')
    for line in inFile:
        if word in line:
            return True
    return False
        
    
def playGame(): #This function plays the word game.
    score = 0
    file = "words_alpha.txt" #The file is a list of words in the English Dictionary.
    timer = threading.Timer(60, allDone) #Once 60 seconds pass, the function 'allDone' is called.
    timer.start()
    row = [[random.choice(upperAlphabet) for i in range(4)] for i in range(5)] #Random letters from 'upperAlphabet' are chosen for the grid.
    for column in range(5):
        print(row[column][0]+" "+row[column][1]+" "+row[column][2]+" "+row[column][3]) #The grid is printed.
            
    while done == False: #'done' is a global variable that is set to 'True' in the function that is called when the timer is done. So this loop runs until the timer is done.
        word = input() #The user inputs a word.
        if word == "":    #The purpose of this if-statement is so that if the user pressed 'enter' to exit the loop (see comments above in the allDone function for why this is necessary), the loop will end without printing the grid again.
            done == True  
        else:
        
            if len(word)>=3 and checkFile(word, file): #The word is valid if it is at least 3 letters long and is found in the dictionary file.
                score += len(word) #The score increases by the length of the word.
                word = word.upper() #word is turned uppercase so that it can be compared to the grid.
                for letter in word: 
                    for column in row:
                        if letter in row[row.index(column)]:
                            row[row.index(column)][column.index(letter)] = random.choice(upperAlphabet) #If a letter was used in a word, it is replaced by a new random letter.
                            break #The break statement is used so that only the first instance of the letter is removed from the grid.
                for column in range(5):
                    print(row[column][0]+" "+row[column][1]+" "+row[column][2]+" "+row[column][3]) #The new grid prints so the user can enter more words.
               
            else:
              print("Not a valid word\n") #If the word was shorter than 3 letters or not found in the dictionary file, it is invalid.
              for column in range(5):
                  print(row[column][0]+" "+row[column][1]+" "+row[column][2]+" "+row[column][3]) #The grid is unchanged, and prints again so the user can continue playing.
    
    #Now that the game loop is over, we print the score:
    print("Your score is "+ (str)(score))
    isHighScore = False
    global highScores  #Makes it so we can add a high score to the global list highScores.
    for s in highScores:
        if score > s[1]: # s[0] is the name, and s[1] is the score.
            isHighScore = True
            print("You got a high score!")
            name = input("Enter your name: ")
            highScores.insert(0, [name, score])
            break   #Break out of the loop so it won't add the score more than once to the list of high scores.
        
    if not isHighScore:  #If the boolean 'isHighScore' is false:
        print("Not a high score.")
    
    showHighScores()
    #Now we return to our menu.
    
def showHighScores():
    if highScores == [['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0], ['',0]]:
        print("There are no high scores yet.")  #If all the high scores are still zero, no high scores are shown.
    else:
        print("\nHigh Scores:")
        for s in highScores:
            if s[1] > 0:  #Only prints high scores if they are greater than zero.
                print(s[0] + ": "+(str)(s[1]))
    
def main():
    userInput = 4
    while userInput>0:
        print("\n")
        userInput = int(input("Anagram Game: \n 1 - Play the game \n 2 - Show high scores \n 3 - Exit the game\n"))
    
        if userInput == 1:
            global done
            done = False
            playGame()  
        elif userInput == 2:
            showHighScores()
        elif userInput == 3:
            print("Exiting game.")
            userInput = 0   #By making this variable = 0, the loop stops and the game is exited.
    

main()

    
        
