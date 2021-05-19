import os,time

class game:
    def __init__(self):
        self.bag = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.p1_hand = []
        self.p2_hand = []


    def bag_length(self):
        return len(self.bag)

#Check if player has lost the game
    def is_lost(self,no_of_stones):
        if no_of_stones < 3:
            if no_of_stones > self.bag_length() or self.bag_length() == 1:
                return False
            else:
                return True
        return True

#Remove the specified number of stones from bag
#Add the stones to current player
    def pick_up_stone(self,player,no_of_stones):
        if player == 'p1':
            for i in range(no_of_stones):
                self.bag.pop(self.bag_length() - 1)
                self.p1_hand.append(0)
            if not self.is_lost(no_of_stones):
                return False
            return True
        if player == 'p2':
            for i in range(no_of_stones):
                self.bag.pop(self.bag_length() - 1)
                if player == 'p2':
                    self.p2_hand.append(0)
            if not self.is_lost(no_of_stones):
                return False
            return True

#Check which player has given the input
def choose_player(no_of_stones,current_player,obj1):
    if no_of_stones == 1 or no_of_stones == 2:
        if current_player == 'p1':
            if not obj1.pick_up_stone('p1',no_of_stones):
                return False
            return True

        elif current_player == 'p2':
            if not obj1.pick_up_stone('p2',no_of_stones):
                return False
            return True
    else:
        print(' Wrong Entry')
        return True

#To run Mulitiplayer mode
def Multiplayer_game(obj1):
    player_1 = input('\n\n Enter Player 1 name: ')
    player_2 = input(" Enter Player 2 name: ")
    os.system('cls')
    while True:
        print('\n\n\t\t\t\t\t\t\tStones Left:',obj1.bag_length())

        no_of_stones = int(input('\n\n %s - Enter Number of stone(1 or 2):'%(player_1)))
        if not choose_player(no_of_stones,'p1',obj1):
            print('\n',player_1,'has won the match')
            return

        no_of_stones = int(input('\n\n %s - Enter Number of stone(1 or 2):'%(player_2)))
        if not choose_player(no_of_stones,'p2',obj1):
            print('\n',player_2,'has won the match')
            return
        print('-'*80)

#Finds the best move of computer
def ai_algo(obj1,safe_point):
    rem = obj1.bag_length()
    if safe_point == rem or safe_point > rem:
        safe_point -= 3
    if rem - safe_point == 2:
        return 2,safe_point
    else:
        return 1,safe_point

#To run AI mode
def AI_game(obj1):
    player_1 = input('\n\n Enter Player 1 name: ')
    os.system('cls')
    safe_point = obj1.bag_length() - 4
    while True:
        print('\n\n\t\t\t\t\t\t\tStones Left:',obj1.bag_length())
        no_of_stones = int(input('\n\n %s - Enter Number of stones(1 or 2):'%(player_1)))
        if not choose_player(no_of_stones,'p1',obj1):
            print('\n',player_1,'has won the match')
            break
        no_of_stones,safe_point = ai_algo(obj1,safe_point)
        #time.sleep(1)
        print("\n\n Stones comp took:",no_of_stones)
        if not choose_player(no_of_stones,'p1',obj1):
            print('\n AI has won the match')
            break
        print('-'*80)



def main():
    obj1 = game()
    os.system('cls')
    print('\t\t\t\tNIM\n\t\t\t   |------------|\n\n')
    print('    Select Mode')
    print('\n\n  *> Press 1 for Multiplayer\n  *> Press 2 for AI\n  *> Press 3 to Quit')
    mode = int(input())
    if mode == 1:
        Multiplayer_game(obj1)
        again = input('Wanna play again(y/n): ')
        if again.lower() == 'y':
            main()
    elif mode == 2:
        AI_game(obj1)
        again = input('\n\n\nWanna play again(y/n): ')
        if again.lower() == 'y':
            main()
    elif mode == 3:
        os.sys.exit()

main()
