symbol1 = str(input("Hi, Welcome to Tic Tac Toe, Player1 which symbol do you wish to choose X or O :")).upper()
symbol2= ""

if symbol1=="X" or symbol1=="O":
    if symbol1 =="X":
        symbol2 = "O"
    else:
        symbol2= "X"
    
    values= [" "," "," "," "," "," "," "," "," "]
    
    def print_grid():
        print(" ")
        print("| {} | {} | {} |".format(values[0], values[1], values[2]))
        print("----------------")
        print("| {} | {} | {} |".format(values[3], values[4], values[5]))
        print("----------------")
        print("| {} | {} | {} |".format(values[6], values[7], values[8]))
        print(" ")
    
    def check_winner(player1):
        poss = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for i in poss:
            if values[i[0]]==values[i[1]]==values[i[2]]!= " ":
                print("congratulations {}, you won!!!".format(player1))
                return True
                break
     
    
    print(" Player 1 symbol: {}".format(symbol1))
    print(" Player 2 symbol: {}".format(symbol2))
    
    print_grid()
    
    for i in range(9):

        value1 = int(input("Player1, please enter your choice: "))
        if values[value1-1] == " " and values[value1-1] != "X" and values[value1-1] != "O":
            values[value1-1] = symbol1
        else:
            print(" The place is already assigned ")
            break
        
        print_grid()
        result = check_winner("player1")
        if result== True:
            break
        
        value2 = int(input("Player2, please enter your choice: "))
        if values[value2-1] == " " and values[value2-1] != "X" and values[value2-1] != "O":
            values[value2-1] = symbol2
        else:
            print(" The place is already assigned ")
            break
        
        print_grid()
        result = check_winner("player2")
        if result== True:
            break
        
         
else:
    print(" ")
    print("please enter correct value")
