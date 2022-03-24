import os,time
os.system('cls')
#--------------------------------------------------------------------#
#INPUT MODULE FOR PLAYER NAMES
#--------------------------------------------------------------------#

Player_1=input("Player 1 Enter Your Name:\t")
Player_2=input("Player 2 Enter Your Name:\t")
print("{} You Have X".format(Player_1))
print("{} You Have O".format(Player_2))
Player1_score=0
Player2_score=0

time.sleep(2)
#--------------------------------------------------------------------#
# TIC TOC TOE LAYOUT FUNCTION TO FOR DISPLAY
#--------------------------------------------------------------------#

def print_board(values):
    os.system('cls')
    #this clears the terminal
    os.system("color A")
    print("-------------------------------------")
    print("-------------TIC-TAC-TOE-------------")
    print("-------------------------------------")
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0][0], values[0][1], values[0][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[1][0], values[1][1], values[1][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[2][0], values[2][1], values[2][2]))
    print("\t     |     |")
    print("\n")

def display_score():
    print("\t   {} - {}   {} - {}".format(Player_1,Player1_score,Player_2,Player2_score))
#---------------------------------------------------------------------------------------
# DEFINING AND INITIALIZE VALUES TO 2D LIST
#---------------------------------------------------------------------------------------
values=[[1],[2],[3]],[[4],[5],[6]],[[7],[8],[9]]
def init_list():
    values[0][0]=" "
    values[0][1]=" "
    values[0][2]=" "
    values[1][0]=" "
    values[1][1]=" "
    values[1][2]=" "
    values[2][0]=" "
    values[2][1]=" "
    values[2][2]=" "
#-------------------------------------------------------------------
#--------------------------------------------------------------------
# FUNCTION TO CHECK WINNER 
#--------------------------------------------------------------------
def winner(values):
    global Player1_score
    global Player2_score
    if values[0][0]=="O" and values[0][1]=="O" and values[0][2]=="O":
        print("{} is WINNERRRR!".format(Player_2))
        Player2_score+=1
        return 0
    elif values[1][0]=="O" and values[1][1]=="O" and values[1][2]=="O":
        print("{} is WINNERRRR!".format(Player_2))
        Player2_score+=1
        return 0
    elif values[2][0]=="O" and values[2][1]=="O" and values[2][2]=="O":
        print("{} is WINNERRRR!".format(Player_2))
        Player2_score+=1
        return 0
    elif values[0][0]=="O" and values[1][0]=="O" and values[2][0]=="O":
        print("{} is WINNERRRR!".format(Player_2))
        Player2_score+=1
        return 0
    elif values[0][1]=="O" and values[1][1]=="O" and values[2][1]=="O":
        print("{} is WINNERRRR!".format(Player_2))
        Player2_score+=1
        return 0
    elif values[0][2]=="O" and values[1][2]=="O" and values[2][2]=="O":
        print("{} is WINNERRRR!".format(Player_2))
        Player2_score+=1
        return 0
    elif values[0][0]=="O" and values[1][1]=="O" and values[2][2]=="O":
        print("{} is WINNERRRR!".format(Player_2))
        Player2_score+=1
        return 0
    elif values[0][2]=="O" and values[1][1]=="O" and values[2][0]=="O":
        print("{} is WINNERRRR!".format(Player_2))
        Player2_score+=1
        return 0
    #--------------------------------------------------------------------#
    elif values[0][0]=="X" and values[0][1]=="X" and values[0][2]=="X":
        print("{} is WINNERRRR!".format(Player_1))
        Player1_score+=1
        return 0
    elif values[1][0]=="X" and values[1][1]=="X" and values[1][2]=="X":
        print("{} is WINNERRRR!".format(Player_1))
        Player1_score+=1
        return 0
    elif values[2][0]=="X" and values[2][1]=="X" and values[2][2]=="X":
        print("{} is WINNERRRR!".format(Player_1))
        Player1_score+=1
        return 0
    elif values[0][0]=="X" and values[1][0]=="X" and values[2][0]=="X":
        print("{} is WINNERRRR!".format(Player_1))
        Player1_score+=1
        return 0
    elif values[0][1]=="X" and values[1][1]=="X" and values[2][1]=="X":
        print("{} is WINNERRRR!".format(Player_1))
        Player1_score+=1
        return 0
    elif values[0][2]=="X" and values[1][2]=="X" and values[2][2]=="X":
        print("{} is WINNERRRR!".format(Player_1))
        Player1_score+=1
        return 0
    elif values[0][0]=="X" and values[1][1]=="X" and values[2][2]=="X":
        print("{} is WINNERRRR!".format(Player_1))
        Player1_score+=1
        return 0
    elif values[0][2]=="X" and values[1][1]=="X" and values[2][0]=="X":
        print("{} is WINNERRRR!".format(Player_1))
        Player1_score+=1
        return 0
#--------------------------------------------------------------------
# FUNCTION FOR CHECKING WHETHER CELL IS EMPTY OR NOT 
#--------------------------------------------------------------------

def check(column,row,value):
    try:
        #if cell of selected row and column is empty
        if values[column][row]==" ":
            values[column][row]=value     
            return
    except IndexError:
        #if user input is out of range
        print("Select within Range 1-3")
    while True:
        try:
            #if cell of selected row is not empty
            print("Not Allowed!")
            print("Plesase Enter row and column {}".format(value))
            column=int(input())-1
            row=int(input())-1
            break
        except (ValueError):
            #if again user input is other than integer.
            print("Value Error. Pleae Enter Correct Input")
    check(column,row,value)   

def save_score():
    f=open("score.txt","a")
    f.write("{} - {}   {} - {}\n".format(Player_1,Player1_score,Player_2,Player2_score))
    f.close()

def game():
#--------------------------------------------------------------------
# LOOP FOR TAKING INPUT FOR ROW AND COLUMNS
#--------------------------------------------------------------------
    for i in range(9):
        if (i)%2==0:
            print("{} , Plesase Enter row and column for X ".format(Player_1))
            value="X"
            while True:
                try:
                    column=int(input())-1
                    row=int(input())-1
                    break
                except (ValueError):
                    #if user input is other than integer.
                    print("That's The Wrong Number")
            check(column,row,value)
        elif(i)%2==1:
            print("{} , Plesase Enter column for O ".format(Player_2))
            value="O"
            while True:
                try:
                    column=int(input())-1
                    row=int(input())-1
                    break
                except (ValueError,IndexError):
                    print("That's The Wrong Number")
            check(column,row,value)
        print_board(values)
#--------------------------------------------------------------------
# CALLING OF WINNER Function
#--------------------------------------------------------------------

        if winner(values)==0:
            display_score()
            play=input("\nRestart Game? (y/n) ")
            if play== 'y':
                init_list()
                print_board(values)
                game()
            elif play=='n':
                save_score()
                break
#--------------------------------------------------------------------
# IF MATCH DRAWS THEN 
#--------------------------------------------------------------------
        if i==8:
            display_score()
            print("\nPlay Again! Match Draw")
            play=input("\nRestart Game? (y/n) ")
            if play == 'y':
                init_list()
                print_board(values)
                game()
            elif(play=='n'):
                save_score()
                break


init_list()
print_board(values)
game()