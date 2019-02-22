
def main():
    print(
    "Bienvenidos a Ana's Gram! \n",
    "[1] Start New Game \n",
    "[2] Continue \n",
    "[3] Quit \n \n",
    "Answer \'Quit\' at any time to exit \n"
)
    choice = input('>')

    if choice == '1':
        print('comenzado nuevo juego...')
        room_selection()
    if choice == '2':
        load_game()
    if choice == '3':
        exit()
    else:
        print("Invalid choice. Choose again.")
        main()
    pass


def la_salon(guess_bank=None):
    #generate dictionary

    word_bank = ['p u e r t a', 's o f a', 't e l e v i s i o n', 'r e l o j', 'l a m p a r a', 'v e n t a n a']
    guess_bank = {}

    for word in word_bank:
        import random
        jumble = word.split(" ")
        word = word.replace(" ", "")
        random.shuffle(jumble)
        guess_bank.update({word: jumble})
        pass

    return guess_bank
    pass

def la_cocina(guess_bank=None):
    #generate dictionary

    word_bank = ['t a z a', 't e n e d o r', 'p l a t o', 't o s t a d o r a', 'f r i g o r i f i c o', 'e s c o b a']
    guess_bank = {}

    for word in word_bank:
        import random
        jumble = word.split(" ")
        word = word.replace(" ", "")
        random.shuffle(jumble)
        guess_bank.update({word: jumble})
        pass

    return guess_bank
    pass

def room_selection():
    print("Abuela: Bienvenidos a mi casa, Ana! Que cuarto? \n",
    "[1] La Salon \n",
    "[2] La Cocina \n")
    choice = input('>')

    if choice == '1':
        la_salon()
        guess_bank = la_salon()
        guess(guess_bank, valid='false')
    if choice == '2':
        la_cocina()
        guess_bank = la_cocina()
        guess(guess_bank, valid='false')
    else:
        print("Invalid Choice. Choose again...")
        room_selection()
    pass


def guess(guess_bank, valid='false'):

    temp = guess_bank

    answers = list(temp.keys())
    anagrams = list(temp.values())

    answer = answers[0]
    anagram = anagrams[0]

    print(anagram, "\n")

    print("nieta, can you tell me what word this is? \n")

    solve = 'false'


    while solve == 'false':
        print(anagram, "\n")
        attempt = input(">")

        if attempt == answer:
            print("Excelente!")

            while valid == 'false':
                again = input("otra vez? [Y] or [N] >")
                if again.lower()== 'n':
                    solve = 'true'
                    valid = 'true'
                    exit()
                    pass
                if again.lower() == 'y':
                    guess_bank.pop(answer)
                    solve = 'true'
                    valid = 'true'

                    check_win(guess_bank)
                    pass
                else:
                    print("Invalid Option")
                    pass

        if attempt.lower() == "quit":
                    quit()
        else:
            print("lo siento, nieta. hacer otra vez.")
            pass
        pass

    pass

def check_win(guess_bank):

    if guess_bank == {}:
        print('You Win!')
        main()
    else:
        guess(guess_bank)
        pass
    pass


def load_game():
    print('sorry, not writen yet')
    pass

if __name__ == "__main__":
    main()
