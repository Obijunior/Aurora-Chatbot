

def Aurora():
    request = input("How can I help you? For a list of commands, type 'help'. : ") 

    if request == 'help':
        print("I am able to : \n Function as a calculator [calculator] \n Set up a two person game of tic-tac-toe[tictactoe]\n Set up a text adventure [rpg]")
        print("How can I help you? ")

    elif request == 'calculator':
        import Calculator

    elif request == 'tictactoe':
        import tictactoe
        
Aurora()
