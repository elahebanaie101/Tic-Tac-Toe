import sys
items = [0,1,2,3,4,5,6,7,8]
def draw_board(items,file_name=None):
    draw_items = (f"{items[0]}|{items[1]}|{items[2]}\n"
                  f"-----\n"
                  f"{items[3]}|{items[4]}|{items[5]}\n"
                  f"-----\n"
                  f"{items[6]}|{items[7]}|{items[8]}\n"
                  f"-----\n")
    if(file_name != None):
        file = open('file.txt','a')
    print(draw_items,file=file if file_name != None else sys.stdout )
    if(file_name != None):
        file.close()
def check_for_win(items):
    #this function returns : 
    # X(when X has won) 
    # or O(when O has won) 
    # or "0-0"(when all fields are taken but no one has won) 
    # or None (when there is at least one empty field and no one has won)
    #Horizental
    if (items[0] == 'X' and items[1] == 'X' and items[2] == 'X'):
        return "X"
    elif  (items[0] == 'O' and items[1] == 'O' and items[2] == 'O'):
        
        return "O"
    elif  (items[3] == 'X' and items[4] == 'X' and items[5] == 'X'):
        
        return "X"
    elif  (items[3] == 'O' and items[4] == 'O' and items[5] == 'O'):
        
        return "O"
    elif  (items[6] == 'X' and items[7] == 'X' and items[8] == 'X'):
        
        return "X"
    elif  (items[6] == 'O' and items[7] == 'O' and items[8] == 'O'):
        
        return "O"
    #Vertical
    if  (items[0] =='X' and items[3] =='X' and items[6]=='X'):
        
        return "X"
    elif ( items[0] =='O' and items[3] =='O' and items[6]=='O'):
        
        return "O"
    elif  (items[1]=='X' and items[4]== 'X'  and items[7] =='X'):
        
        return "X"

    elif  (items[1]=='O' and items[4]== 'O' and items[7] == 'O'):
        
        return "O"

    elif  (items[2]=='X' and items[5]=='X' and items[8] == 'X'):
        
        return "X"

    elif  (items[2]=='O'and  items[5]=='O' and items[8]== 'O'):
        
        return "O"

    #Cross
    if  (items[0]== 'X' and items[4]== 'X' and items[8]== 'X'):
        
        return "X"
    elif  (items[0]== 'O' and items[4]== 'O' and items[8]== 'O'):
        
        return "O"
    if  (items[2]== 'X' and items[4]== 'X' and items[6]== 'X'):
        
        return "X"
    elif  (items[2]== 'O' and items[4]== 'O' and items[6]== 'O'):
        
        return "O"
    
    count_of_taken_fields = 0 
    for item in items : 
        if(item == "X" or item == "O"):
            count_of_taken_fields += 1
    return "0-0" if count_of_taken_fields == 9 else None #when it has reached here it means none of earlier---
    # ----returns has worked and it means that no one has won yet so game is either equal or not finished
def draw_line_seperator():
    print(' - - - - - - - - ')
def select_best_option(items):
    #this function checks and put O where putting O there causes computer to win 
    #Horizental
    if items[0]=='O'and items[1]=='O':
       if items[2] != 'X':
          items[2] = 'O'
    elif items[1]=='O'and items[2]=='O':
         if items[0] != 'X':
            items[0] = 'O'
    elif items[0]=='O'and items[2]=='O':
         if items[1] != 'X':
            items[1] = 'O'

    elif items[3]=='O'and items[4]=='O':
        if items[5] != 'X':
           items[5] = 'O'
    elif items[4]=='O'and items[5]=='O':
        if items[3] != 'X':
         items[3] = 'O'
    elif items[3]=='O'and items[5]=='O':
        if items[4] != 'X':
         items[4] = 'O'
    elif items[6]=='O'and items[7]=='O':
        if items[8] != 'X':
         items[8] = 'O'
    elif items[7]=='O'and items[8]=='O':
        if items[6] != 'X':
         items[6] = 'O'
    elif items[6]=='O'and items[8]=='O':
        if items[7] != 'X':
         items[7] = 'O'
    #Vertical
    elif items[0]=='O'and items[3]=='O':
        if items[6] != 'X':
         items[6] = 'O'
    elif items[0]=='O'and items[6]=='O':
        if items[3] != 'X':
         items[3] = 'O'
    elif items[3]=='O'and items[6]=='O':
        if items[0] != 'X':
         items[0] = 'O'

    elif items[1]=='O'and items[4]=='O':
        if items[7] != 'X':
         items[7] = 'O'
    elif items[1]=='O'and items[7]=='O':
        if items[4] != 'X':
         items[4] = 'O'
    elif items[4]=='O'and items[7]=='O':
        if items[1] != 'X':
         items[1] = 'O'

    elif items[5]=='O'and items[2]=='O':
        if items[8] != 'X':
         items[8] = 'O'
    elif items[8]=='O'and items[2]=='O':
        if items[5] != 'X':
         items[5] = 'O'
    elif items[5]=='O'and items[8]=='O':
        if items[2] != 'X':
         items[2] = 'O'
    #Cross
    elif items[0]=='O'and items[4]=='O':
        if items[8] != 'X':
         items[8] = 'O'
    elif items[0]=='O'and items[8]=='O':
        if items[4] != 'X':
         items[4] = 'O'
    elif items[4]=='O'and items[8]=='O':
        if items[0] != 'X':
         items[0] = 'O'
    elif items[4]=='O'and items[2]=='O':
        if items[6] != 'X':
         items[6] = 'O'
    elif items[6]=='O'and items[2]=='O':
        if items[4] != 'X':
         items[4] = 'O' 
    elif items[4]=='O'and items[6]=='O':
        if items[2] != 'X':
         items[2] = 'O'

def block_lose(items):
    #this function checks and put O where putting X there causes user to win 
    #Horizental
    if items[0] == 'X' and items[1] == 'X':
        if items[2] != 'O':
           items[2] = 'O'
        return True
    elif items[0] == 'X' and items[2] =='X':
        if items[1] != 'O':
           items[1] = 'O' 
        return True   
    elif items[1] == 'X' and items[2] =='X':
        if items[0] != 'O':
           items[0] = 'O'   
        return True
    elif items[3] == 'X' and items[4] =='X':
         if items[5] != 'O':
            items[5] = 'O'  
         return True  
    elif items[4] == 'X' and items[5] =='X':
        if items[3] != 'O':
          items[3] = 'O' 
        return True   
    elif items[3] == 'X' and items[5] =='X':
        if items[4] != 'O':
           items[4] = 'O'    
        return True
    elif items[6] == 'X' and items[7] =='X':
        if items[8] != 'O':
           items[8] = 'O'
        return True    
    elif items[7] == 'X' and items[8] =='X':
        if items[6] != 'O':
           items[6] = 'O' 
        return True   
    elif items[6] == 'X' and items[8] =='X':
        if items[7] != 'O':
           items[7] = 'O'
        return True   
    #Vertical 
    elif items[0] == 'X' and items[3] =='X':
        if items[6] != 'O':
           items[6] = 'O'
        return True    
    elif items[0] == 'X' and items[6] =='X':
        if items[3] != 'O':
           items[3] = 'O'
        return True    
    elif items[3] == 'X' and items[6] =='X':
        if items[0] != 'O':
           items[0] = 'O'
        return True    

    elif items[1] == 'X' and items[4] =='X':
        if items[7] != 'O':
           items[7] = 'O'
        return True    
    elif items[1] == 'X' and items[7] =='X':
        if items[4] != 'O':
           items[4] = 'O'
        return True    
    elif items[4] == 'X' and items[7] =='X':
        if items[1] != 'O':
           items[1] = 'O'
        return True    

    elif items[2] == 'X' and items[5] =='X':
        if items[8] != 'O':
           items[8] = 'O'    
        return True
    elif items[5] == 'X' and items[8] =='X':
        if items[2] != 'O':
           items[2] = 'O'
        return True    
    elif items[8] == 'X' and items[2] =='X':
        if items[5] != 'O':
           items[5] = 'O'
        return True    
    #Cross
    elif items[0] == 'X' and items[4] =='X':
        if items[8] != 'O':
           items[8] = 'O'
        return True    
    elif items[0] == 'X' and items[8] =='X':
        if items[4] != 'O':
           items[4] = 'O'
        return True    
    elif items[4] == 'X' and items[8] =='X':
        if items[0] != 'O':
           items[0] = 'O'
        return True    
    elif items[4] == 'X' and items[2] =='X':
        if items[6] != 'O':
           items[6] = 'O'
        return True    
    elif items[6] == 'X' and items[2] =='X':
        if items[4] != 'O':
           items[4] = 'O'
        return True    
    elif items[4] == 'X' and items[6] =='X':
        if items[2] != 'O':
           items[2] = 'O'
        return True
    return False
def fill_places(items):
    if items[0] == 0:
        items[0] = 'O'
    elif items[2] == 2:
        items[2] = 'O'
    elif items[6] == 6:
        items[6] = 'O'
    elif items[8] == 8:
        items[8] = 'O'
    elif items[4] == 4:
        items[4] = 'O'
    elif items[1] == 1:
        items[1] = 'O'
    elif items[3] == 3:
        items[3] = 'O'
    elif items[5] == 5:
        items[5] = 'O'
    elif items[7] == 7:
        items[7] = 'O'