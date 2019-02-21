def main():
    print(
    "Bienvenidos a Ana's Gram! \n",
    "[1] Start New Game \n",
    "[2] Continue \n",
)
    choice = input('>')

    if choice == '1':
        print('comenzado nuevo juego...')
        room_selection()
    if choice == '2':
        load_game()
    else:
        print('Sorry, not an option!')
    pass

def room_selection():
    print("Abuela: Bienvenidos a mi casa, Ana! Que cuarto? \n",
    "[1] La Salon (Living Room) \n",
    "[2] La Cocina - Kitchen \n")
    choice = input('>')

    if choice == '1':
        la_salon()
    if choice == '2':
        la_cocina()
    pass

def la_salon(answer=None):
    #generate dictionary

    word_bank = ['p u e r t a', 's o f a', 't e l e v i s i o n', 'r e l o j']
    guess_bank = {}

    for word in word_bank:
        import random
        jumble = word.split(" ")
        word = word.strip()
        random.shuffle(jumble)
        print(jumble)
        guess_bank.update({word: jumble})
        print(guess_bank)
        pass


    pass

def load_game():
    print('sorry, not writen yet')
    pass

if __name__ == "__main__":
    main()
