import random

class RPS:
    rounds=0; turn=0; stage=0; win=0; user_win_count=0; pc_win_count=0; ties=0
    def __init__(self, round):
        rounds=round; win=0; user_win_count=0; pc_win_count=0; ties=0
  
    def player(self):
        choices = input('Enter R for rock, P for paper and S for scissors ')
        return choices
  
    def computer(self):
        list2=['R', 'P', 'S']
        pc=random.choice(list2)
        print('Computer generated: ', pc)
        return pc

    def evaluate(self, r2, move_user, move_pc, round_no):
        descion=0; WIN_U=r2.user_win_count; WIN_PC=r2.pc_win_count; TIE=r2.ties
        if move_user=='R' and move_pc=='R':
            print('Tie')
            descion='Tie'
            TIE+=1
            win=0
        elif move_user=='P' and move_pc=='P':
            print('Tie')
            descion='Tie'
            TIE+=1
            win=0
        elif move_user=='S' and move_pc=='S':
            print('Tie')
            descion='Tie'
            TIE+=1
            win=0
        elif move_user=='R' and move_pc=='P':
            print('User wins')
            descion='User wins'
            WIN_U=WIN_U+1
            win=1
        elif move_user=='R' and move_pc=='S':
            print('User wins')
            descion='User wins'
            WIN_U=WIN_U+1
            win=1
        elif move_user=='P' and move_pc=='R':
            print('PC wins')
            descion='PC wins'
            WIN_PC=WIN_PC+1
            win=2
        elif move_user=='P' and move_pc=='S':
            print('PC wins')
            descion='PC wins'
            WIN_PC=WIN_PC+1
            win=2
        elif move_user=='S' and move_pc=='R':
            print('PC wins')
            descion='PC wins'
            WIN_PC=WIN_PC+1
            win=2
        elif move_user=='S' and move_pc=='P':
            print('User wins')
            descion='User wins'
            WIN_U=WIN_U+1
            win=1
        if round_no==1:
            print("Final results: ")
            if WIN_U>WIN_PC and WIN_U>TIE:
                print('User Wins the game')
            elif WIN_U<WIN_PC and WIN_PC>TIE and WIN_U<TIE:
                print('PC Wins the game')
            elif WIN_U>WIN_PC and WIN_PC<TIE:
                print('User Wins the game')
            elif WIN_U==WIN_PC and WIN_PC<TIE or WIN_U<TIE:
                print('Game Tied')
            elif WIN_U==TIE and WIN_U>WIN_PC:
                print('User Wins the game')
            elif WIN_U==TIE and WIN_U<WIN_PC:
                print('PC Wins the game')
            elif WIN_PC==TIE and WIN_U<WIN_PC:
                print('PC Wins the game')
            elif WIN_PC==TIE and WIN_U>WIN_PC:
                print('User Wins the game')
            elif TIE>WIN_PC and TIE>WIN_U:
                print('Game Tied')
        return descion


round=int(input('Enter the number of rounds: '))
list=[0, 1]
p1=RPS(round)
ro=round
while round>0:
    turns=random.choice(list)
    user1=p1.player()
    pc1=p1.computer()
    p1.evaluate(p1, user1, pc1, round)
    round=round-1