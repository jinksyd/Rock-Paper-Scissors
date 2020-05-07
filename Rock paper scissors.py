x = input("Please enter rock, paper, or scissors: ")
y = input("Please enter rock, paper, or scissors: ")

def compare(x, y):
    
    if x == y:
        return("you have tied")
    elif x == 'rock':
        if y == 'scissors':
            return("Rock wins")
        else:
            return("Paper wins")
    elif x == 'scissors':
        if y == 'paper':
            return("Scissors wins")
        else:
            return("Rock wins")
    elif x == 'Paper':
        if y == 'scissors':
            return("Scissors wins")
        else:
            return("Rock wins")
    else:
        return("Invalid, please enter rock, paper, or scissors")

print(compare(x, y))