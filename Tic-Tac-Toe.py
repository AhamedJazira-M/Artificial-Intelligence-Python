import math
board=['-']*9
you= input("Enter your choice 'X' OR 'O' :")
if (you=='X'):
       AI='O'
       print("AI plays with 'O'")
else:
       AI='X'
       print("AI plays with 'X'")
       
def print_board(board):
       for i in range(0,9,3):
              print(board[i] + "|" + board[i+1] + "|" + board[i+2])
       print()  
def winner(board,player):
       combinations=[
              [0,1,2],[3,4,5],[6,7,8],
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6]]
       for combo in combinations:
              if all(board[i]==player for i in combo):
                     return True
       return False
def full(board):
       return all(cell!='-' for cell in board)
def minimax(board,depth,alpha,beta,maxplayer):
       if winner(board,AI):
              return 1
       elif winner(board,you):
              return -1
       elif full(board):
              return 0
       if maxplayer:
              maxi=-math.inf
              for i in range(9):
                     if board[i]=='-':
                            board[i]=AI
                            eval=minimax(board,depth+1,alpha,beta,False)
                            board[i]='-'
                            maxi=max(maxi,eval)
                            alpha=max(alpha,eval)
                            if beta<=alpha:
                                   break
              return maxi
       else:
              mini=math.inf
              for i in range(9):
                     if board[i]=='-':
                            board[i]=you
                            eval=minimax(board,depth+1,alpha,beta,True)
                            board[i]='-'
                            mini=min(mini,eval)
                            beta=min(beta,eval)
                            if beta<=alpha:
                                   break
              return mini
def findbest(board):
       bestmove=-1
       besteval=-math.inf
       for i in range(9):
              if board[i]=='-':
                     board[i]=AI
                     eval=minimax(board,0,-math.inf,math.inf,False)
                     board[i]='-'
                     if eval > besteval:
                            besteval=eval
                            bestmove=i
       return bestmove
while True:
       print_board(board)
       move=int(input("Enter your position[0-8]:"))
       if board[move]=='-':
              board[move]=you
              if winner(board,you):
                     print_board(board)
                     print("YOU WON!")
                     break
              elif full(board):
                     print_board(board)
                     print("IT'S A DRAW!")
                     break
              ai_move=findbest(board)
              board[ai_move]=AI
              if winner(board,AI):
                     print_board(board)
                     print("AI WINS!")
                     break
              elif full(board):
                     print_board(board)
                     print("IT'S A DRAW!")
                     break
       else:
              print("Cell already filled. TRY AGAIN.")
              