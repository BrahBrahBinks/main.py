import random
import os
import time


# Main.py 
#Derik Nguyen

name = input("What is your name? ")
#asks user to assign a name

def sprint1():
    #Sprint 1 Program ie. basic computation, simple I/O

    print("Hello World, i AM pc ", end = "!\n")
    #end adds on to end of print statement

    #name = input("What is your name? ")
    # asks user to assign a name

    print("OK", name+",","Let's go over numeric operators!")
    #prints name inputted before

    print("PEMDAS\n")

    print("Parentheses () even in computer programmming" ,
          " are performed first.", sep = '', end = "\n\n")
    #sep allows commas in print statement to be substituted for something other than a space

    print("Exponentiation ** is denoted by two stars instead of a ^.\n" +
          "For example 2 ** 3 =", 2 ** 3, end = "\n\n")
    #exponentiation 2^3 is denoted as 2**3

    print("Multiplication * is denoted using only a * and never an x.\n" +
          "For example 2 * 3 =", 2 * 3, end = "\n\n")
    #multiplication *

    print("Division is denoted by the / symbol.\n" + "For example 9 / 3 =", format(9/3, ".0f"), end = "\n\n")
    #division /

    print("There are other types of division as well in programming,\ncalled "
          "floor division(//) and modulo division(%)")
    #modulo division and floor division

    print("Floor division // allows division into te lowest possible "
          "integer.\n" + "For example 10 // 3 =", 10//3, end = "\n\n")
    # //

    print(
        'Modulo division % returns the remainder of a division if it '
        'doesn\'t divide perfectly, otherwise it returns zero')
    print("For example, 10 % 2 =", 10 % 2, "and 10 % 3 =", str(10 % 3) + ".")
    # %

    print("Addition and Subtraction are still denoted using a + and a -.\n" +
          "For example 2 + 3 =", 2 + 3, "and 2 - 3 =", 2 - 3, end = ".\n\n")
    # +/-

    print("Concatonation of strings is done with a +")
    print("Concatonation" + " of" + " strings" + " is" + " done" + " with" +
          " a" + " +")
    # string concatonation is done using "+" in python


    time.sleep(10)
    os.system('cls')
    print(" Error 404 SYSTEM LOADING" * 100)
    # string multiplication is done using "*" in python
    time.sleep(5)
    os.system("cls")










def yes_no_menu(game):
    while True:
        choice = ''
        while choice != 'y' and choice != 'n':
                
            print(f"Okay {name}, do you want to play {game}? y/n")
            choice = str(input())
            #print(choice)
            if choice == 'y':
                print("Have fun!")
                return 0
                break
            elif choice == 'n':
                print('thats to bad')
                time.sleep(1)
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





def play_hangman():
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

    # Word bank of animals
    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()
    # code taken from internet to make art and word bank:
    #  https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

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

def play_bottles():
    
    for i in range(99, 0, -1):
        b = i - 1
        c = (f'{i} bottles of beer on the wall, {i} bottles of beer, take one down pass it around, {b} bottles of beer on the wall!')

        if c == '1 bottles of beer on the wall, 1 bottles of beer, take one down pass it around, 0 bottles of beer on the wall!':
            c = c.replace('bottles', 'bottle', 2)
            print(c)
        else:
            print(c, '\n')
        time.sleep(.2)
    return 0



def a_full_class():
    print('George has the same number of male classmates',
          'as female classmates. His classmate Sandra has',
          'three-fourths as many female classmates as male classmates.',
          'How many students are in the class? Try to use loops to check',
          'plausible combinations, and stop when you found the answer.')
    for i in range(0,20):
        totalmales = 1 + i
        totalfems = totalmales - 1
        ratio = (totalfems - 1) / (totalmales)
        if ratio == .75:
            print("total females is:", totalfems)
            print("total males is:", totalmales)

def play_blackjack():
    blackjack = 0
    while blackjack <= 21:
        decide = input('Hit or pass: H or P ').upper()
        if decide == 'H':
            blackjack += random.randint(1,11)
            print(blackjack)
            if blackjack == 21:
                print('you win')
                break
    print('you bust')


 
def string_abacus(value):
    populate = ''
    number = int(value)
    string1 = str(number)
    abacus = '00000*****'
    rows = 10 - len(string1)
    while rows > 0:
        populate += '|00000*****   |\n'
        rows -= 1
    for num in string1:
        populate += ('|' + abacus[:len(abacus)-int(num)] + '   ' + abacus[len(abacus)-int(num):] + '|\n')
    return populate
def play_abacus():
    while True:
        
        try:
            number = int(input("enter a number: "))
            abacus = string_abacus(number)
            print(abacus)
            break
        except ValueError:
            print("That was not a valid number. Please try again: ")






def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if year1 < year2:           #this makes sure year1 is the newer year
        year1, year2 = year2, year1
        month1, month2 = month2, month1
        day1, day2 = day2, day1


    leaps1 = 0                #counts the leap years in the range of a given year not counting the year itself

    for x in range(1,year1):
        if x % 4 == 0 and not x % 100 == 0 or x % 400 == 0:
            leaps1 += 1
                
    nonleaps1 = year1 - leaps1
    totaldays1 = (nonleaps1*365) + (leaps1*366)


    leaps2 = 0

    for y in range(1,year2):
        if y % 4 == 0 and not y % 100 == 0 or y % 400 == 0:
            leaps2 += 1

    nonleaps2 = year2 - leaps2
    totaldays2 = (nonleaps2*365) + (leaps2*366)


    jan, mar, may, jul, aug, octe, dec = 31, 31, 31, 31, 31, 31, 31
    apr, jun, sep, nov = 30, 30, 30, 30
    feb = 28

    january = 0
    february = jan
    march = february + feb
    april = march + mar
    maiy = april + apr
    june = maiy + may
    july = june + jun
    august = july + jul
    september = august + aug
    october = september + sep
    november = october + octe
    december = november + nov

    if month1 == 1:
        month1 = january
    elif month1 == 2:
        month1 = february
    elif month1 == 3:
        month1 = march
    elif month1 == 4:
        month1 = april
    elif month1 == 5:
        month1 = maiy
    elif month1 == 6:
        month1 = june
    elif month1 == 7:
        month1 = july
    elif month1 == 8:
        month1 = august
    elif month1 == 9:
        month1 = september
    elif month1 == 10:
        month1 = october
    elif month1 == 11:
        month1 = november
    else:
        month1 = december

    
    if month2 == 1:
        month2 = january
    elif month2 == 2:
        month2 = february
    elif month2 == 3:
        month2 = march
    elif month2 == 4:
        month2 = april
    elif month2 == 5:
        month2 = maiy
    elif month2 == 6:
        month2 = june
    elif month2 == 7:
        month2 = july
    elif month2 == 8:
        month2 = august
    elif month2 == 9:
        month2 = september
    elif month2 == 10:
        month2 = october
    elif month2 == 11:
        month2 = november
    else:
        month2 = december

    monthndays1 = month1 + day1
    monthndays2 = month2 + day2
    if year1 % 4 == 0 and not year1 % 100 == 0 or year1 % 400 == 0:
        if monthndays1 > 59 and day1 != 29:
            monthndays1 += 1
    if year2 % 4 == 0 and not year2 % 100 == 0 or year2 % 400 == 0:
        if monthndays2 > 59 and day2 != 29:
            monthndays2 += 1


    total1 = monthndays1 + totaldays1
    total2 = monthndays2 + totaldays2

    final = total1 - total2
    if final < 0:
        final = - final
    return final




def play_days():

    while True:
        a = int(input('Enter year1: '))
        b = int(input('Enter month1: '))
        c = int(input('Enter day1: '))
        d = int(input('Enter year2: '))
        e = int(input('Enter month2: '))
        f = int(input('Enter day2: '))
        print(daysBetweenDates(a, b, c, d, e, f), 'days between dates or roughly', daysBetweenDates(a, b, c, d, e, f) / 365, 'years' )
        final = input('replay? y/n ')
        if final == 'n':
            break



def replay():
    while True:
        
        replay = input('Would you like to play again? yes or no: ').lower()
        if replay == 'yes':
            return 0
            break
        elif replay == 'no' or replay == 'No':
            print("Thanks for playing!")
            return 1
            break
            
        else:
            print("I don't understand that...")
            time.sleep(2) 
        
  

def calc():
    print('''
            This is a correct change calculator, 
            it will ask for the price of an item and the amount
            paid by the customer. 
            The program will then render the exact change to be returned
            Enter values in this format: 00.00 without a dollar sign
            ''') 
#there is a problem with floats not giving proper values so program had to be written in terms of integers
    sentinel = 0
    while sentinel == 0:
        price = input('Enter the price of an item: ')
        pay = input('How much did the customer give you? ')
        pricecal = float(price) * (10**2)
        paycal = float(pay) * (10**2)
        dif = int(paycal) - int(pricecal)
        diff = int(dif)
        #print(diff)
        count_dollars = 0
        count_quartz = 0
        count_dimes = 0
        count_nicks = 0
        count_pens = 0
        while diff > 0:
            if diff >= 100:
                diff -= 100
                count_dollars += 1
            elif diff >= 25:
                diff -= 25
                count_quartz += 1
            elif diff >= 10:
                diff -= 10
                count_dimes += 1
            elif diff >= 5:
                diff -= 5
                count_nicks += 1
            else:
                diff -= 1
                count_pens += 1

        #print(diff)
        print('Your change is:')
        print(f'                         {str(count_dollars)} dollars')
        print(f'                         {str(count_quartz)} quarters')
        print(f'                         {str(count_dimes)} dimes')
        print(f'                         {str(count_nicks)} nickels')
        print(f'                         {str(count_pens)} pennies')
        sentinel = replay()

    




def play_pokemon():
    from random import randint as ran
    from time import sleep as zzz

    p1health = 100
    p2health = 100


    #messages

    print('''
    How to play
    Moves:
    Quick Attack--Q-- High Probability Low Damage
    Heavy Attack--H-- Low Probability High Damage
    Heal----------X-- Medium Probability
    ''')
    while p1health > 0 and p2health > 0: #play the game while both players have life
        numbergen1 = ran(1,100)
        numbergen2 = ran(1,100)   #generates values of 1-100
    
        move1 = -ran(18,25)
        move2 = -ran(45,70)
        move3 = ran(18,65)    #heal
    
        decision1 = input('Choose a move: ').upper()
        if decision1 not in 'QHX':
            print('''I don't understand''')
        else:
            if decision1 == 'Q' and numbergen1 >= 30:
                p2health += move1
                print('player chooses quick attack and was successful')
                print('quick attack does', move1, 'damage')
            elif decision1 == 'H' and numbergen1 >= 70:
                p2health += move2
                print('player chooses heavy attack and was successful')
                print('heavy attack does', move2, 'damage')
            elif decision1 == 'X' and numbergen1 >= 50:
                p1health += move3
                print('player chooses heal and was successful')
                print('heal does', move3, 'health')
            else:
                print('player move unsuccessful')
        botmove = ran(1,3)
        if botmove == 1 and numbergen2 >= 30:
            p1health += move1
            print('bot chooses quick attack and was successful')
            print('quick attack does', move1, 'damage')
        elif botmove == 2 and numbergen2 >= 70:
            p1health += move2
            print('bot chooses heavy attack and was successful')
            print('heavy attack does', move2, 'damage')
        elif botmove == 3 and numbergen2 >= 50:
            p2health += move3
            print('bot chooses heal and was successful')
            print('heal does', move3, 'health')
        else:
            print('bot move unsuccessful')
        if p2health > 0 and p1health > 0:
            print('bot health =', p2health)
            print('player health =', p1health)
        
    print('Game Over')    
    if p1health > 0:
        print('you win!')
    else:
        print('you lose')

    zzz(5)


def multiplication_tables():
    
    number = int(input('Enter a number here to get a multiplication table: '))
    if number < 0:
        number = -number   #this line deals with neg integers put into input
    output = ''            #this variable is the one that gets populated
    count = number         #this is the count set outside the while loop
    while count > 0:
        for i in range(1, 13):
            result = i * count
            string = str(result) + ' '  #composes the string to output
            output += string        #populates output variable
        output += '\n' #this line creates rows for the multiplication table
        count -= 1     #this closes the while loop
    print(output)










  


def magic_8():
    a = 'All signs point to yes'
    b = "That doesn't seem likely"
    c = 'No, I would give up now'
    d = 'Do more research'
    e = 'It is fated in the stars'
    f = 'You must be joking'
    g = 'Yes'
    h = 'Of course!'
    i = 'Anything is possible if you just believe'
    j = 'something, something, Battlestar Gallactica'
    k = 'What gave you that idea?'
    l = 'no...'
    m = 'maybe baby'
    n = 'YOLO right?'
    o = "sorry, she's just not that into you"
    p = 'may the odds be ever in your favor'

    info = input('Ask a yes or no question > ')
        
    if '?' in info:
        
        print('processing...')
        time.sleep(3)
        choice = random.randint(1,16)
    else:
        print("I don't understand that...")
        time.sleep(3)
        magic_8()

    if choice == 1:
        print(a)
    elif choice == 2:
        print(b)
    elif choice == 3:
        print(c)
    elif choice == 4:
        print(d)
    elif choice == 5:
        print(e)
    elif choice == int('6'):
        print(f)
    elif choice == int('7'):
        print(g)
    elif choice == 8:
        print(h)
    elif choice == int('9'):
        print(i)
    elif choice == int('10'):
        print(j)
    elif choice == int('11'):
        print(k)
    elif choice == 12:
        print(l)
    elif choice == int('13'):
        print(m)
    elif choice == int('14'):
        print(n)
    elif choice == int('15'):
        print(o)
    else:
        print(p)
    time.sleep(2)

 
    





def main():
    play = yes_no_menu('a game')
    if play == 0:
        games = ['bottles', 'hangman', 'blackjack', 'abacus', 'between dates',
                 'calculator', 'pokemon','multiplication tables','magic 8 ball']
        index = 0
        for game in (games):
            play = yes_no_menu(games[index])

            if play == 0 and index == 0:
                play_bottles()
            
            elif play == 0 and index == 1:
                play_hangman()
            elif play == 0 and index == 2:
                play_blackjack()
            elif play == 0 and index == 3:
                play_abacus()
            elif play == 0 and index == 4:
                play_days()
            elif play == 0 and index == 5:
                calc()
            elif play == 0 and index == 6:
                play_pokemon()
            elif play == 0 and index == 7:
                multiplication_tables()
            elif play == 0 and index == 8:
                magic_8()
            #elif play == 0 and index == 10:
            #elif play == 0 and index == 11:
            #elif play == 0 and index == 12:
            index += 1
        else:
            print("goodbye")
            time.sleep(1)
    else:
        print("")
sprint1()
main()

