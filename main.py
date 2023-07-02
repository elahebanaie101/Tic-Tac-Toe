#computer is always "O" and user is "X"
from random import choice
from helper import check_for_win , select_best_option , block_lose , fill_places , draw_board , draw_line_seperator
items = [0,1,2,3,4,5,6,7,8]

def give_input_from_computer():
    global items 
    draw_board(items)
    tmp = items.copy()
    select_best_option(tmp)
    if(check_for_win(tmp) == "O"):
        select_best_option(items)
        print('computer selected a field')
        draw_board(items)
        print('O won')
        draw_line_seperator()
        return
    tmp = items.copy()
    if(block_lose(tmp) == True):
        block_lose(items)
    else:
        fill_places(items)

    print('computer selected a field')
    draw_board(items)
    draw_line_seperator()
    if(check_for_win(items) == "X" or check_for_win(items) == "O"):
        print(f'{check_for_win(items)} won')
        return 
    elif(check_for_win(items) == "0-0"):
        print('game finished but no one won ')
        return
    else:
        give_input_from_user()
def give_input_from_user():
    global items 
    draw_board(items)
    tmp = input("Choose a number[0-8]: ")
    if(tmp.isdigit()):
        chosen_number = int(tmp)
    else:
        give_input_from_user()
    if (chosen_number>=0 and chosen_number<=8):
        if items[chosen_number] == 'X' or items[chosen_number] ==  'O':
           print("your chosen place is taken,choose another one")
           give_input_from_user()
        else:
            items[chosen_number] = "X"
            draw_board(items)  
            if(check_for_win(items) == "X" or check_for_win(items) == "O"):
                print(f'{check_for_win(items)} won')
                draw_line_seperator()
                return 
            else:
                draw_line_seperator()
            give_input_from_computer()
    else:
        print("invalid input. choose a num between [0-8]")
        give_input_from_user()
participants =['player','computer']
whoseturn = choice(participants)
if whoseturn == 'player':
    print("it's your turn to play")
    give_input_from_user()
else:
    print("it's computer's turn to play")
    give_input_from_computer()
    