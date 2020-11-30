

def Aurora():
    request = input("How can I help you? For a list of my commands, type 'help'. : ") 

    if request == 'help':
        print("I am able to : \n Function as a calculator [calculator] \n Set up a two person game of tic-tac-toe[tictactoe]\n Set up a text adventure [rpg]")
        Aurora()

    elif request == 'calculator'or request == 'Calculator':
        from Calculator import str_or_flt
        str_or_flt()
        Aurora()

    elif request == 'tictactoe':
        from tictactoe import game
        game()
        Aurora()

    elif request == 'rpg':
      from RPG import rpg
      rpg()
      Aurora()  
Aurora()
