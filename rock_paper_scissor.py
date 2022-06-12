
def descision(x, y):
    if player1 == 'rock' and player2 == 'scissor':
        print("rock beats scissor")
    elif player1 == 'scissor' and player2 == 'rock':
        print("rock beats scissor")
    elif player1 == 'scissor' and player2 == 'paper':
        print("Scissor beats paper")
    elif player1 == 'paper' and player2 == 'scissor':
        print("Scissor beats paper")
    elif player1 == 'paper' and player2 == 'rock':
        print("Paper beats rock")
    elif player1 == 'rock' and player2 == 'paper':
        print("Paper beats rock")
    elif player1 == player2:
        print("Nullified")
    else:
        print("Invalid input")

print("Type rock paper scissor to select:\n")
player1 = input("player1: Enter the input:\n")
player2 = (input("Player2: Enter the input:\n"))
player1 = player1.lower()
player2 = player2.lower()
descision(player1,player2)
