randomNumber = 8
guessedNumberInput = input("Guess a number between 1 and 9: ")
guessedNumber = guessedNumberInput
chances = 5
while chances < 6:

        if guessedNumber==8:
                print("Congratulation, you guessed the correct number!")
                break        
        elif chances==0:
                print("You lose, the number is", randomNumber)
                break
        else:
                chances = chances -1
                print("wrong number, think again")
                guessedNumber = input("Guess a number between 1 and 9: ")

        
   