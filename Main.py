import random
import os
import time


# Main.py 
#Derik Nguyen


#Sprint 1 Program ie. basic computation, simple I/O

print("Hello World, i AM pc ", end = "!\n")
#end adds on to end of print statement

name = input("What is your name? ")
#asks user to assign a name 

print("OK", name+",","Let's go over numeric operators!")
#prints name inputted before

print("PEMDAS\n")

print("Parentheses () even in computer programmming" , " are performed first.", sep = '', end = "\n\n")
#sep allows commas in print statement to be substituted for something other than a space

print("Exponentiation ** is denoted by two stars instead of a ^.\n" + "For example 2 ** 3 =", 2 ** 3, end = "\n\n")
#exponentiation 2^3 is denoted as 2**3

print("Multiplication * is denoted using only a * and never an x.\n" + "For example 2 * 3 =", 2 * 3, end = "\n\n")
#multiplication *

print("Division is denoted by the / symbol.\n" + "For example 9 / 3 =", format(9/3, ".0f"), end = "\n\n")
#division /

print("There are other types of division as well in programming,\ncalled floor division(//) and modulo division(%)")
#modulo division and floor division

print("Floor division // allows division into te lowest possible integer.\n" + "For example 10 // 3 =", 10//3, end = "\n\n")
# //

print("Modulo division % returns the remainder of a division if it doesn't divide perfectly, otherwise it returns zero")
print("For example, 10 % 2 =", 10 % 2, "and 10 % 3 =", str(10 % 3) + ".")
# %

print("Addition and Subtraction are still denoted using a + and a -.\n" + "For example 2 + 3 =", 2 + 3, "and 2 - 3 =", 2 - 3, end = ".\n\n")
# +/-

print("Concatonation of strings is done with a +")
print("Concatonation" + " of" + " strings" + " is" + " done" + " with" + " a" + " +")
# string concatonation is done using "+" in python


time.sleep(10)

print(" Error 404 SYSTEM LOADING" * 100)
# string multiplication is done using "*" in python
time.sleep(5)






os.system("cls")
hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
#code taken from internet to make art and word bank:
#  https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c


def main_menu():
    while True:
        choice = ''
        while choice != 'y' and choice != 'n':
                
            print(f"Okay {name}, do you want to play hangman? y/n")
            choice = str(input())
            print(choice)
            if choice == 'y':
                print("Enjoy the game!")
                return 0
                break
            elif choice == 'n':
                print('thats to bad')
                return 1
                break
            else:
                print("invalid input")
        break
    return 0


def ask():
    print("Please choose a letter: ")
    letter = str(input())
    return letter





def play_game():
    
    mystery_word = words[random.randint(0,len(words))]
    #print(mystery_word)            
    list_word = sorted(mystery_word)

    no_dupes_list_word = []
    for i in list_word:
        if i not in no_dupes_list_word:
            no_dupes_list_word.append(i)

    no_dupes_list_word = sorted(no_dupes_list_word)
    #print(no_dupes_list_word)
    right_guesses = ''
    list_right_guesses = []
    death = -1
    print("Here's a hint for you, the mystery word starts with this character:",
          mystery_word[0])
    #print(list_word)
    while death < 6:
        
        guess = ask()
        if guess in mystery_word:
     
            if guess not in right_guesses:
                right_guesses += guess
                list_right_guesses += guess
                print(right_guesses, sep = '')
                list_right_guesses = sorted(list_right_guesses)
                print("You got it dude!")
                #print(list_right_guesses)
            else:
                print("Already in memory bank")
            time.sleep(1)
            os.system("cls")
            #print(no_dupes_list_word)
            #print(list_right_guesses)
            if no_dupes_list_word == list_right_guesses:
                print("mystery word is", mystery_word)
                print("You win!")
                time.sleep(1)
                break
        else:
            print("No, that's not right")
            death += 1
            if death > 0:
            
                print (hangman_pics[death])




def main():
    play = main_menu()
    if play == 0:
        
        play_game()
    else:
        print("goodbye")
        time.sleep(1)
main()
